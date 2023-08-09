import re
import subprocess

print("********** Now Playing **********")
try:
    # Fetch media sessions
    raw_out = subprocess.check_output(
    "adb shell dumpsys media_session", shell=True).decode("utf-8")

    # Write a regex to match MediaSession...(Not followed by Helper) till the next empty line
    pat = re.compile(r"(?:MediaSession|MediaButtonControl)(?!Helper).*?\n\n", re.DOTALL)

    # Write a regex to match the uid
    pat1 = re.compile(r"ownerUid=(\d+)", re.DOTALL)

    # Write a regex to match the last played audio playback
    pat2 = re.compile(r"Audio playback.*?uid=(\d+)", re.DOTALL)

    # Write a regex to match the description
    pat3 = re.compile(r"description=(.*?)\n", re.DOTALL)


    matches = pat.findall(raw_out)
    sessions = {
        pat1.search(match).group(1): match for match in matches
    }

    last_played = pat2.search(raw_out).group(1)

    # print(sessions[last_played])
    print(pat3.search(sessions[last_played]).group(1))

except Exception as e:
    print(f"Error: {e}")
    print("Please make sure that the device is connected and media is playing")

# Fetch audio format details
# print("********** Audio Format **********")
try:
    raw_out = subprocess.check_output(
        "adb logcat -s \"bt_a2dp_hw\" -e \"out_write\" -d | tail -4"
        , shell=True).decode("utf-8")
    # Remove the log prefix till the last occurence of "out_write"
    raw_out = '\n'.join([
        line.split("out_write:     ")[1] for line in raw_out.split("\n")[1:-1]
    ])

    print(raw_out)

except Exception as e:
    print(f"Error: {e}")
    print("Please make sure that the device is connected and media is playing")



print("************************************")