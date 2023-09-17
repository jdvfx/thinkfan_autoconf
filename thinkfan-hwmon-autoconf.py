
"""
for thinkfan.conf
print all the temperature sensors
with name and indices
can be copied to the start of thinkfan.conf

"""

import glob
import re
import os

hwmon_sensors = []

for hwmon in glob.glob("/sys/class/hwmon/*"):
    name = ""
    indices = []
    for hwmon_name in glob.glob(hwmon+"/name"):
        with open(hwmon_name,"r") as f:
            name = f.read().splitlines()[0]
    for temp_input in glob.glob(hwmon+"/temp*_input"):
        with open(temp_input,"r") as g:
            try:
                g.read()
                file_name = os.path.basename(temp_input)
                hwmon_indices = [int(s) for s in re.findall(r'\d', file_name)]
                indices.extend(hwmon_indices)
            except Exception:
                print(">ERR, could not read:",temp_input)
                print("-- sensor ignored --")


    if(len(indices)>0):
        indices.sort()
        hwmon_sensor = [hwmon,name,indices]
        hwmon_sensors.append(hwmon_sensor)

hwmon_sensors.sort()
print("\nsensors:")
for sensor in hwmon_sensors:

    title = sensor[1].upper()
    print(f"  # {title}")
    print(f"  - hwmon: {sensor[0]}")
    print(f"    name: {sensor[1]}")
    print(f"    indices: {sensor[2]}")
print("")
