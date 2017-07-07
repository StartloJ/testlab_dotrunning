import sys
import time
maxLoop = 1000
while(maxLoop > 0):
    sys.stdout.write('.')
    maxLoop -= 1
    time.sleep(0.5)