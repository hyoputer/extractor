#-*- coding:utf-8 -*-
import os
import shutil
import re

os.system('rd /s /q files')
os.system('mkdir files')

checklist = open("checklist.txt", 'r', encoding='utf-8', errors='ignore')
cklist = checklist.readlines()

exception = open("exception.txt", 'r', encoding='utf-8', errors='ignore')
ecps = exception.readlines()

filelist = []
dirlist = []
ckendlist = []
ecplist = []
ecpendlist = []

for ck in cklist:
  if (ck.rstrip()[-1] == '\\'):
    dirlist.append(ck.rstrip()[:-1])
  elif (ck[0] == '*'):
    ckendlist.append(ck.rstrip()[1:])
  else:
    filelist.append(ck.rstrip())

for ecp in ecps:
  if (ecp[0] == '*'):
    ecpendlist.append(ecp.rstrip()[1:])
  else:
    ecplist.append(ecp.rstrip())

filespath = os.path.join(os.getcwd(), "files")

tmp = os.listdir(os.getcwd())
for dirname in tmp:
  dirpath = os.path.join(os.getcwd(), dirname)
  if os.path.isdir(dirpath) and dirpath != filespath:
    for (path, dir, files) in os.walk(dirpath):
      dirflag = False
      for ckdir in dirlist:
        if ckdir in path:
          dirflag = True
          
      for filename in files:
        copyflag = True
        if not dirflag:
          copyflag = False
          fullpath = os.path.join(path, filename)
          for ckname in filelist:
            if ckname.lower() == filename.lower():
              copyflag = True
          for ckend in ckendlist:
            if filename.lower().endswith(ckend.lower()):
              copyflag = True

        for ecpname in ecplist:
          if ecpname.lower() == filename.lower():
            copyflag = False
        for ecpend in ecpendlist:
          if filename.lower().endswith(ecpend.lower()):
            copyflag = False

        if copyflag:
          target = open(fullpath, 'r', encoding='utf-8', errors='ignore')
          data = target.read()
          txtpath = os.path.join(filespath, dirname + '.txt')
          if os.path.isfile(txtpath):
            txt = open(txtpath, 'a', encoding='utf-8', errors='ignore')
          else:
            txt = open(txtpath, 'w', encoding='utf-8', errors='ignore')
          txt.write(filename+ '\n')
          txt.write(data + '\n')