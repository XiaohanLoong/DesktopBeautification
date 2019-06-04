import os
import random

def execCmd(cmd):
    return os.popen(cmd).read()

msg = execCmd("fortune -e tang300 song100")
re = ('[', '2', '3', 'm', '\x1b')
for i in re:
    msg = msg.replace(i, "")
print(msg[:-1])
