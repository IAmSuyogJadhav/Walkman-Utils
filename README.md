# Walkman-Utils
A collection of scripts I wrote for use with my Walkman NW-A105.


### `walkman_audio_log.py`
This script will display information about the current audio playback on the Walkman. Currently only shows this information for *bluetooth (LDAC)* playback. An example output is shown below:
Requires the device to be connected to a computer via USB with debugging enabled. Also requires the `adb` tools to be installed on the computer.

```
********** Now Playing **********
Man in the Long Black Coat, Bob Dylan, Oh Mercy
flags=Direct|Offload(0x11), handle=0x6d
direct : 96000Hz ST(0x3) PCM32(0x3)
effect.processor: 96000Hz 2ch S32_LE
************************************
```

The first line is the name of the track, as reported by the player. The rest of the lines show additional information about the audio quality. The `flags` line shows the flags that are set for the current audio playback. `Direct|Offload(0x11)` seems to be what the best quality playback will look like on LDAC (appears with the native Sony music player, and some specific third party apps such as UAPP that communicate directly with the internal DAC).
The third and fourth lines show the frequency and the bit depth of the audio (source and sink, respectively). The `direct` line shows the frequency and the bit depth of the audio that is being sent to the Walkman's bluetooth chip. The `effect.processor` line shows the frequency and the bit depth of the audio that is being sent to the Walkman's DAC. You can check to make sure that the source sample rate matches your audio file. The bit depth, as long it is higher or equal to the one reported by your audio file, makes no difference to the actual audio quality. Check if the `direct` and the `effect.processor` frequencies match, which should be the case for the best quality playback, withouth any resampling. The last part of the last two lines shows the bit depth of the audio. `PCM32` means 32-bit, `PCM24` means 24-bit, and `PCM16` means 16-bit. The `S32_LE` means that the audio. Note that, sometimes these may not match even in the best quality playback if your bluetooth headphones do not support a sample rate/bit depth that high. Also check to make sure LDAC is enabled and set to "sound quality preferred" in the Walkman's bluetooth settings.


Currently only works with UAPP, and the native music player. Planning to add support for more apps in the future.
