import os
import shutil

os.system('rm -r files')
os.system('mkdir files')

checklist = open("checklist.txt", 'r')
cklist = checklist.readlines()

filelist = []
extlist = []

for ck in cklist:
  if (ck[0] == '.'):
    extlist.append(ck.rstrip())
  else:
    filelist.append(ck.rstrip())

filespath = os.path.join(os.getcwd(), "files")

tmp = os.listdir(os.getcwd())
for dirname in tmp:
  dirpath = os.path.join(os.getcwd(), dirname)
  if os.path.isdir(dirpath) and dirpath != filespath:
    for (path, dir, files) in os.walk(dirpath):
      for filename in files:
        copyflag = False
        fullpath = os.path.join(path, filename)
        for ckname in filelist:
          if ckname.lower() == filename.lower():
            copyflag = True
        ext = os.path.splitext(filename)[-1]
        for extname in extlist:
          if extname.lower() == ext.lower():
            copyflag = True

        if copyflag:
          target = open(fullpath, 'r')
          data = target.read()
          txtpath = os.path.join(filespath, dirname + '.txt')
          if os.path.isfile(txtpath):
            txt = open(txtpath, 'a')
          else:
            txt = open(txtpath, 'w')
          txt.write(data + '\n')