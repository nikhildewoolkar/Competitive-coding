import os
import subprocess
cmdf = 'cd Desktop'
os.system(cmdf)
print("located to desktop")

cmd = 'g++ compiler.cpp -o a.exe'
os.system(cmd)
o=subprocess.check_output("cmd", shell=True, universal_newlines=True)
print(o)
cmd = 'a.exe'
os.system(cmd)
returned_text = subprocess.check_output("a.exe", shell=True, universal_newlines=True)
print(returned_text)
