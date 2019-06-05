import os

files_dirs = os.listdir('.')
for file_dir in files_dirs:
    if os.path.isdir(file_dir):
        cmd = r"zip -r %s.zip %s/*" % (file_dir.replace(' ', '\ '), file_dir.replace(' ', '\ '))
        os.system(cmd)
