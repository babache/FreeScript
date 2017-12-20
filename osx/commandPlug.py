from pyHS100 import SmartPlug, SmartBulb, Discover
from pprint import pformat as pf
import subprocess
import re
import time

ip = ""
for dev in Discover.discover().values():
    ip = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", str(dev)).group(0)
exit
if ip == "":
   exit

plug = SmartPlug(ip)

output = subprocess.check_output(['pmset', '-g', 'batt'])
percent = re.search(r"\d{1,3}%", str(output)).group(0)
battery = int(percent.replace('%', ''))

if int(battery)>95 and plug.state == "ON":
    print ("Turn OFF at %s" % time.strftime("%d/%m/%Y %H:%M:%S"))
    plug.turn_off()

if int(battery)<20 and plug.state == "OFF":
    print ("Turn ON at %s" % time.strftime("%d/%m/%Y %H:%M:%S"))
    plug.turn_on()
