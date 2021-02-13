import os
import sys
import time


imf = '\ZCHelper.exe'

exe = sys.executable
dname = os.path.dirname(exe)
utp = os.path.split(dname)
os.chdir(utp[0])
puti = str(utp[0]) + imf


try: w = os.system('taskkill /f /im  ZCHelper.exe')
except Exception: pass


if w == 0: time.sleep(2)


os.startfile(puti,'runas')
sys.exit()

