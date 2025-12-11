import os
import subprocess
import sys
import time

time.sleep(5)
os.replace("NiloyHUBNew.exe","NiloyHUBGui.exe")
subprocess.Popen(["NiloyHUBGui.exe"])
sys.exit()