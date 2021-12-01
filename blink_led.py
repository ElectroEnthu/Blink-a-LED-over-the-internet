from boltiot import Bolt
import conf,time

mybolt = Bolt(conf.api_key,conf.device_id)

while True:
    on = mybolt.digitalWrite('0','HIGH')
    print(on)
    time.sleep(1) #1 second delay
    off = mybolt.digitalWrite('0','LOW')
    print(off)
    time.sleep(1) #1 second delay
