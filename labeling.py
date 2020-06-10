import os
import shutil

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
    idx = 1
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
          shutil.copy(fullpath, filespath)
          os.rename(os.path.join(filespath, filename), os.path.join(filespath, dirname + str(idx) + '-' + filename))
          idx+=1