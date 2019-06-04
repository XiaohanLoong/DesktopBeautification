import os
import threading
interval = 5
def execCmd(cmd):
    result = os.popen(cmd)
    text = result.read()
    result.close()
    return text

def change():
    pic_path = "/home/loongxiaohan/Pictures/i3"
    cmd = "cd %s &&  ls | sort -R | head -1" % pic_path
    pic_url = execCmd(cmd).replace('\n', '')
    ch_cmd = ('gsettings set org.gnome.desktop.background picture-uri file:"%s/%s"' % (pic_path, pic_url))
    os.system(ch_cmd)

def func_time():
    change()
    timer = threading.Timer(interval, func_time)
    timer.start()

timer = threading.Timer(interval,func_time)  #首次启动
timer.start()
