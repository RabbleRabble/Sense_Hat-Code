import os
import random
import time
from sense_hat import SenseHat

sense = SenseHat ()
sense.set_rotation(180)
sense.clear()


def fix_temp(temp, cpu, r, g, b, rb, gb, bb):
    temp = ((temp - ((cpu - temp)/2))-6)
    temp = (temp * 1.8) + 32
    temp = round(temp)
    sense.show_message("T:" + str(temp), text_colour=[r, g, b], back_colour=[rb, gb, bb])


while True:
    temp_t = sense.get_temperature()
    temp_h = sense.get_temperature_from_humidity()
    temp_p = sense.get_temperature_from_pressure()
    temp = (temp_t + temp_h + temp_p)/3
    t = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cputemp = t.read()
    cputemp = cputemp.replace ('temp=','')
    cputemp = cputemp.replace('\'C\n','')
    cputemp = float(cputemp)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rb = random.randint(0, 255)
    gb = random.randint(0, 255)
    bb = random.randint(0, 255)

    while (r==rb and g==gb and b==bb) or (r==0 and g==0 and b==0):
        if r==rb and g==gb and b==bb:
            rg = random.randint(0, 255)
            gb = random.randint(0, 255)
            bb = random.randint(0, 255)
        elif r==0 and g==0 and b==0:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            
        
    hum = sense.get_humidity()
    hum = round(hum)

    fix_temp(temp, cputemp, r, g, b, rb, gb, bb)

    sense.show_message("H:" + str(hum), text_colour=[r, g, b], back_colour=[rb, gb, bb])

    time.sleep(4)
