DEVICE_ID = "device_id"
DEVICE_IP = "device_ip.ip.ip.ip"
DEVICE_KEY = "device_key"

PLUG_ID = "plug_id"
PLUG_IP = "plug_ip.ip.ip.ip"
PLUG_KEY = "plug_key"

import tinytuya

d = tinytuya.BulbDevice(DEVICE_ID, DEVICE_IP, DEVICE_KEY)
d.set_version(3.3)
data = d.status()
#print('Dictionary %r' % data)

d.set_white(255,255)
d.set_brightness(1000)

e = tinytuya.OutletDevice(PLUG_ID, PLUG_IP, PLUG_KEY)
e.set_version(3.3)
data = e.status()
e.turn_on()
