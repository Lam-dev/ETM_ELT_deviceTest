import subprocess
from subprocess  import Popen, PIPE

proc = Popen("sudo hwclock -f /dev/rtc0 -r".split(" "),stdout=PIPE)
proc.stdin.write("lamnguyen96")
response ,_= proc.communicate()

print(response)
