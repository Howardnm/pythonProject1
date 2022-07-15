#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

list1=[]
ppp=''


def gci(filepath):
    # 遍历filepath下所有文件，包括子目录
    files=os.listdir(filepath)
    for fi in files:
        fi_d=os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:
            print(os.path.join(filepath, fi_d))
            ppp=os.path.join(filepath, fi_d)
            list1.append(ppp)
            # print(list1)


# 递归遍历/root目录下所有文件
gci('/volume1/Resilio Sync/folders/plex_music')

fo=open("/volume1/Resilio Sync/folders/foo.txt", "w+", encoding='utf8')
for line in list1:
    fo.writelines(line + "\n")
fo.close()

print(list1)

# 读取绝对路径，识别"/"，将列表内元素细分，形成套娃列表
fo = open("/volume1/Resilio Sync/folders/foo.txt", "r")
ls = []
for line in fo:
    line = line.replace("\n","")
    ls.append(line.split("/"))
print(ls)
fo.close()

fo=open("/volume1/Resilio Sync/folders/foo.txt", "w+", encoding='utf8')
fo.writelines(ls)
fo.close()