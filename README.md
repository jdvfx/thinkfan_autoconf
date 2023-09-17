example output:<br>

```
>ERR, could not read: /sys/class/hwmon/hwmon6/temp8_input
-- sensor ignored --

sensors:
  # ACPITZ
  - hwmon: /sys/class/hwmon/hwmon1
    name: acpitz
    indices: [1]
  # NVME
  - hwmon: /sys/class/hwmon/hwmon3
    name: nvme
    indices: [1, 2, 3]
  # AMDGPU
  - hwmon: /sys/class/hwmon/hwmon4
    name: amdgpu
    indices: [1]
  # K10TEMP
  - hwmon: /sys/class/hwmon/hwmon5
    name: k10temp
    indices: [1]
  # THINKPAD
  - hwmon: /sys/class/hwmon/hwmon6
    name: thinkpad
    indices: [1, 2, 3, 4, 5, 6, 7]

```

usage:

```:python thinkfan-hwmon-autoconf.py```

replace the ```sensors:``` section in ```/etc/thinkfan.conf```
make sure to keep the ```fans:``` and ```levels:```





