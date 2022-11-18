# 有问题提交Issue https://github.com/WadeChenn/Plex-SortTittle
# 或联系 yerwer@foxmail.com
# 库名参数-l (库名或 all ) -n (库编号) -c (是否覆盖 1 or 0) -log(1 or 0 是否打开进度条log)
#########################参数初始化(使用配置文件请修改此处)############################
USE_INIT=True                               #使用当前配置请设为True,否则将尝试从外部获取参数
PLEX_TOKEN="mXYRmTzBe5VxkPKysW7u"            #Plextoken获取,具体方法请自行查找 "zZzxxxxxxxJssiw2zcy" *必须设置
PLEX_URL="http://bueess.top:32400"         #Plexurl "http://plex.xxx.cn:32400" *必须设置
RECOVER=1                               #是否覆盖已有的拼音排序
LIB_NAME=''                                 #要排序的库名(存在时库编号不生效)
LIB_NUMBER=0                                #要排序的库编号(不使用库编号则设为0)
ENABLE_LOG=1                                #是否输出进度条
MEDIA_ID=0
##############################################################

import os
from importlib import import_module
from pickle import FALSE, TRUE
import sys
import urllib

#########################依赖库初始化###########################
# 依赖库列表
import_list=[
    'pypinyin',
    'plexapi',
    'argparse'
]
# 判断依赖库是否安装,未安装则安装对应依赖库
sourcestr = "https://pypi.tuna.tsinghua.edu.cn/simple/"  # 镜像源
def GetPackage(PackageName):
    comand = "pip install " + PackageName +" -i "+sourcestr
    # 正在安装
    print("------------------正在安装" + str(PackageName) + " ----------------------")
    print(comand + "\n")
    os.system(comand)
for v in import_list:
    try:
        import_module(v)
    except ImportError:
        print("Not find "+v+" now install")
        GetPackage(v)
##############################################################

import pypinyin
from plexapi.server import PlexServer
import re
import argparse




def uniqify(seq):
    keys = {}
    for e in seq:
        keys[e] = 1
    return keys.keys()


def check_contain_chinese(check_str):  # Judge chinese
    for ch in check_str:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def chinese2pinyin(chinesestr): #chinese to pyinyin
    pyinyin_list = []
    pinyin = pypinyin.pinyin(chinesestr, style=pypinyin.FIRST_LETTER,heteronym=True)
    for i in range(len(pinyin)):
        pyinyin_list.append(str(pinyin[i][0]).upper())
    pyinyin_str = ''.join(pyinyin_list)
    return pyinyin_str

def removePunctuation(query):
    # 去除标点符号（只留字母、数字、中文)
    if query:
        rule = re.compile(u"[^a-zA-Z0-9]")
        query = rule.sub('', query)
    return query
tags = {
        "Action":"动作",
        "Adventure":"冒险",
        "Animation" :"动画",
        "Anime" : "动画",
        "Mini-Series" : "短剧",
        "War & Politics" : "政治",
        "Sci-Fi & Fantasy" : "科幻",
        "Suspense" : "悬疑",
        "Reality" : "记录",
        "Comedy":"喜剧",
        "Crime":"犯罪",
        "Documentary":"纪录",
        "Drama":"剧情",
        "Family":"家庭",
        "Fantasy":"奇幻",
        "History":"历史",
        "Horror":"恐怖",
        "Music":"音乐",
        "Mystery":"悬疑",
        "Romance":"爱情",
        "Science Fiction":"科幻",
        "Sport":"体育",
        "Thriller":"惊悚",
        "War":"战争",
        "Western":"西部",
        "Biography":"传记",
        "Film-noir":"黑色",
        "Musical":"音乐",
        "Sci-Fi":"科幻",
        "Tv Movie":"电视",
        "Disaster":"灾难",
        "Children" :"儿童",
        "Martial Arts":"武术",
        "Talk":"访谈",
        }
def updategenre(video,genres):
    englist=[]
    chlist=[]
    for tag in genres:
        enggenre = tag.tag
        if enggenre in tags.keys():
            englist.append(enggenre)
            zhQuery = tags[enggenre]
            chlist.append(zhQuery)
    if len(englist) >0: 
        video.addGenre(chlist, locked=False)
        video.removeGenre(englist, locked=False)

def singleVideo(video):
    title = video.title
    video._edit_tags(tag="actor", items=[x.tag for x in video.actors], remove=True)
    if video.titleSort:  # 判断是否已经有标题
        con = video.titleSort
        if (check_contain_chinese(con) or RECOVER):
            SortTitle = chinese2pinyin(title)
            SortTitle=removePunctuation(SortTitle)
            try:
                video.editSortTitle(SortTitle)
            except:
                print("Edit SortTitle error")
    if video.genres:
        genres=video.genres
        updategenre(video,genres)
        #     continue
        # continue

def loopThroughAllMovies(videos):
    print("正在进行索引请稍候...")
    video_len=len(videos.all())
    for video,i in zip(videos.all(),range(video_len)):
        video.reload()
        j=int(i/video_len*100)
        if i==video_len-1:
            j=100
        if ENABLE_LOG:
            print("\r", end="")
            print("进度: {}%: ".format(j), "▓" * (j // 2)," " * (50-j // 2), end=str(i+1)+"/"+str(video_len))
            sys.stdout.flush()
        title = video.title
        if video.titleSort:  # 判断是否已经有标题
            con = video.titleSort
            if (check_contain_chinese(con) or RECOVER):
                SortTitle = chinese2pinyin(title)
                SortTitle=removePunctuation(SortTitle)
                try:
                    video.editSortTitle(SortTitle)
                except:
                    print("Edit SortTitle error")
            #     continue
            # continue
        if video.genres:
            genres=video.genres
            updategenre(video,genres)

if __name__ == '__main__':

    parse_xls = argparse.ArgumentParser(description="parse arguement of SortTittle")
    parse_xls.add_argument('-url', nargs='?', default=None)
    parse_xls.add_argument('-token', nargs='?', default=None)
    parse_xls.add_argument('-c', nargs='?', default=0)
    parse_xls.add_argument('-n', nargs='?', default=0)
    parse_xls.add_argument('-l', nargs='?', default='')
    parse_xls.add_argument('-log', nargs='?', default=1)
    parse_xls.add_argument('-mid', nargs='?', default=0)

    #get param
    if USE_INIT==False:
        parse_argument = parse_xls.parse_args()
        # PLEX_URL=parse_argument.url
        # PLEX_TOKEN=parse_argument.token
        RECOVER=parse_argument.c
        LIB_NAME=parse_argument.l
        LIB_NUMBER=parse_argument.n
        ENABLE_LOG=parse_argument.log
        MEDIA_ID=parse_argument.mid
    if ENABLE_LOG:
        print("--------------------------------------")
        print("正在连接PLEX服务器...")
        print("PLEX_URL = "+PLEX_URL)
        print("PLEX_TOKEN = "+PLEX_TOKEN)
    try:
        plex = PlexServer(PLEX_URL, PLEX_TOKEN)
    except:
        print("plex url 或 token错误!")
        os._exit()
    if ENABLE_LOG:
        print("服务器连接成功")
        print("--------------------------------------")
        print("Start Serching!")
        print("--------------------------------------")
    libtable=[]
    # ddd=plex.library.search(guid='plex://movie/5d7768d2ebdf2200209c912f')
    # print(ddd)
    # ddd=plex.library.search(id=8904)
    # print(ddd)
    for section in plex.library.sections():
        # if section.type == 'show' or section.type =='movie':
        print(section.title,section.key)
        # print(section.collections.title)

        libtable.append(section.title)
    # for collection in plex.library.collections():
        # print(collection.title,collection.key)
        # libtable.append(section.title)
    print("--------------------------------------")
    # MEDIA_ID=8905
    if MEDIA_ID:
        video=plex.library.search(id=MEDIA_ID)
        # plex.library.
        singleVideo(video[0])
    else:
        if len(LIB_NAME)>0:
            if LIB_NAME =="all":
                print("All libs Start!")
                # loopThroughAllMovies(plex.library)
                # print("\n排序成功!")
                for i in range(len(libtable)):
                    print("\nStart NO."+str(i)+" "+libtable[i])
                    videos = plex.library.section(libtable[i])
                    loopThroughAllMovies(videos)
                print("\n排序成功!")
            else:
                print("指定库为:"+LIB_NAME+" Start!")
                try:
                    videos = plex.library.section(LIB_NAME)
                    loopThroughAllMovies(videos)
                    print("\n排序成功!")
                except:
                    print("库名错误!")

        else:
            if LIB_NUMBER != 0:
                try:
                    videos = plex.library.sectionByID(int(LIB_NUMBER))
                    loopThroughAllMovies(videos)
                    print("\n排序成功!")
                except:
                    print("出错!")
                    os._exit()
            else:
                print("未设定库名")
                LIB_NUMBER = input('请输入你要排序的库编号：')
                LIB_NUMBER=int(LIB_NUMBER)
                try:
                    videos = plex.library.sectionByID(LIB_NUMBER)
                    loopThroughAllMovies(videos)
                    print("\n排序成功!")
                except:
                    print("出错!")
                    os._exit()



