import os
import random
import time
from sense_hat import SenseHat

sense = SenseHat ()
sense.set_rotation(180)
sense.clear()

while True:
    t = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cputemp = t.read()
    cputemp = cputemp.replace ('temp=','')
    cputemp = cputemp.replace('\'C\n','')
    cputemp = float(cputemp)

    cputemp = (cputemp * 1.8) + 32
    cputemp = round(cputemp)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    sense.show_message (str(cputemp), text_colour=[r,g,b])

    time.sleep(5)
