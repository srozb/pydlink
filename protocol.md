# D-Link babycam DL-820L communication protocol description

## Main

|HTTP endpoint|read parameters|write parameters|description|
|---|---|---|---|
|`/config/user_mod.cgi`|?|name, password|user modify|
|`/users/verify.cgi`|group||auth/role verification|
|`/config/camera_info.cgi`|name, location|name, location|device identification|
|`/common/info.cgi`|model, product, brand, version, build, nipca, name, location, macaddr, ipaddr, netmask, gateway, wireless, inputs, outputs, speaker, videoout, pir, icr, ir, mic, led, td, playing_music||device info|
|`/users/babycam_info.cgi`|||another way to list the device info|
|`/config/led.cgi`|led|led|toggle camera control leds|
|`/config/datetime.cgi`|method, timeserver, timezone, utcdate, utctime, date, time, dstenable, dstauto, offset, starttime, stoptime|timeserver, more?|date/time settings|
|`/users/bootup_music.cgi`|enable|enable|toggle boot up sound|

## Wireless

|HTTP endpoint|read parameters|write parameters|description|
|---|---|---|---|
|`/config/wireless.cgi`|enable, mode, essid, chpatterns, channel, auth, encryption, passphrase|?|Wifi client settings|
|`/config/wireless_ap.cgi`|enable, essid, security, key|?|Wifi access-point settings (default AP name & password)|
|`/config/wlansurvey.cgi`|||wifi scanner|

## SD card

|HTTP endpoint|read parameters|write parameters|description|
|---|---|---|---|
|`/config/sdcard.cgi`|status, total, used, free||sdcard storage stats|
|`/config/sdcard_list.cgi`|sd_status, path, page, pagesize, total_file, total_page, num, items|path||
|`/config/sdcard_download.cgi`|path, file, result|path, file|download sdcard item|
|`/music/sdcard_music_list.cgi`|sd_status, path, page, pagesize, total_file, total_page, num, items|path||
|`/config/sdcard_format.cgi`||format=go|format sd card|

## Sensors

|HTTP endpoint|read parameters|write parameters|description|
|---|---|---|---|
|`config/speaker.cgi`|enable, volume|enable, volume||
|`/config/icr.cgi`|mode, light_threshold_list, light_threshold|mode, light_threshold_list, light_threshold|night/day toggle|
|`/config/auto_pan.cgi`||act=go||
|`/config/ptz_preset.cgi`||name, act||
|`/config/ptz_direction.cgi`||direction, speed||
|`/config/motion.cgi`|enable, mbmask, sensitivity|enable, mbmask, sensitivity|motion detection settings|
|`/config/audio_detection.cgi`|enable ,sensitivity|enable, sensitivity|noise detection settings|
|`/config/thermal_detection.cgi`||enable, high_detect, low_detect, high_threshold, low_threshold, unit||
|`/config/sensor.cgi`|brightness, contrast, saturation, whitebalance, flicker, maxexposuretime, mirror, flip, color|?|camera image settings|
|`/config/speaker.cgi`|enable, volume| enable, volume|speaker settings|
|`/users/env_sound_lv.cgi`|||?|

## Capture

|HTTP endpoint|read parameters|write parameters|description|
|---|---|---|---|
|`/image/jpeg.cgi`|-|-|Capture JPEG|
|`/video/ACVS-H264.cgi`|-|profileid|Capture video stream|
|`/audio/ACAS-AAC.cgi`|-|profileid|Capture audio stream|


## Lullaby

|HTTP endpoint|read parameters|write parameters|description|
|---|---|---|---|
|`/music/sys_music_play.cgi`|file, loop, shuffle, timer|file, loop, shuffle, timer|play a lullaby|
|`/music/music_stop.cgi`|||stop playback|
|`/music/sdcard_play.cgi`||file||

## Other

|HTTP endpoint|read parameters|write parameters|description|
|---|---|---|---|
|`/cgi/admin/recorder.cgi`|-|-||

## Other other...

* /cgi/admin/adv_wizard.cgi
* /cgi/admin/recorder.cgi
* /cgi/admin/tools_admin.cgi
* /cgi/admin/st_device.cgi
* /cgi/admin/reboot.cgi
* /cgi/admin/tools_default.cgi
* /cgi/admin/tools_firmware.cgi
* /cgi/admin/tools_system.cgi
