from dataclasses import replace
import music_tag
import os
import requests
import json
import time
import re
# pip3 install requests


token='secret_DkYKff6IQJdGJTqgFslKQqGpLtsu44RiH3Vsa2nhYjO'

databaseId='8b7919e4ec944391a82fa0a80a8e7212'

headers={
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13",
    'Cache-Control': 'no-cache'
}

music_files='/volume1/Resilio Sync/folders/plex_music'
music_list_cache1="/volume1/Resilio Sync/folders/foo1.txt"
music_list_cache2="/volume1/Resilio Sync/folders/foo2.txt"
music_artist=6

music_list=[]  # 读取绝对路径，识别"/"，将列表内元素细分，形成套娃列表
music_list_AP=[]  # 读取绝对路径，写入列表
num=0
GB_size=""
json_file1=""
music_tag_format1, music_tag_album, music_tag_year="", "", ""

# 遍历本地音乐文件

def find_music():
    print("运行find_music")
    list1=[]
    def gci(filepath):
        ppp=''
        # 遍历filepath下所有文件，包括子目录
        files=os.listdir(filepath)
        for fi in files:
            fi_d=os.path.join(filepath, fi)
            if os.path.isdir(fi_d):
                gci(fi_d)
            else:
                # print(os.path.join(filepath, fi_d))
                ppp=os.path.join(filepath, fi_d)
                list1.append(ppp)
                # print(list1)

    # 递归遍历/root目录下所有文件
    gci(music_files)

    # 遍历后的绝对路径，写入txt
    fo=open(music_list_cache1, "w+", encoding='utf8')
    for line in list1:
        fo.writelines(line + "\n")
    fo.close()
    # print(list1)

    # 删除包含".sync"的行
    list2=[]
    matchPattern=re.compile(r'.sync')
    file=open(music_list_cache1, 'r')
    while 1:
        line=file.readline()
        if not line:
            print("读取文件结束 or 出错")
            break
        elif matchPattern.search(line):
            pass
        else:
            list2.append(line)
    file.close()
    file=open(music_list_cache1, 'w')
    for i in list2:
        file.write(i)
    file.close()

    # 读取绝对路径，写入列表
    fo=open(music_list_cache1, "r")
    for line in fo:
        line=line.replace("\n", "")
        music_list_AP.append(line)
    fo.close()
    print("----------------")
    print(music_list_AP)
    # 读取绝对路径，识别"/"，将列表内元素细分，形成套娃列表
    fo=open(music_list_cache1, "r")
    for line in fo:
        line=line.replace("\n", "")
        music_list.append(line.split("/"))
    print(music_list)
    fo.close()
    # 整理后的列表重新写入
    fo=open(music_list_cache2, "w+", encoding='utf8')
    fo.write(str(music_list))
    fo.close()


# 检索文件夹大小
def osos(folder_path):
    full_size=sum(sum(os.path.getsize(os.path.join(parent, file)) for file in files) for parent, dirs, files in
                  os.walk(folder_path))
    global GB_size
    GB_size="%.2f GB" % (full_size / 1024 / 1024 / 1024)
    print("%.2f GB" % (full_size / 1024 / 1024 / 1024))


# notion

# 下载notion-json
def readDatabase(databaseId, headers):
    print("执行readDatabase")
    global json_file1
    readUrl=f"https://api.notion.com/v1/databases/{databaseId}/query"

    res=requests.request("POST", readUrl, headers=headers)
    data=res.json()
    print(res.status_code)
    print(res.text)
    json_file1=res.text
    # print(json_file1)
    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


# 下载notion-json，提取每一行的id
def removeLine():
    print("执行removeLine")
    global num, num4, token, databaseId, headers, json_file1, dict1
    try:
        test1=dict1.get('results')[0]
    except IndexError:
        print("已清空列表")
    else:
        try:
            data={'archived': True}
            page_id=dict1.get('results')[num].get('id')  # "提取每一行id"
            print(dict1.get('results')[num].get('id'))
            response = requests.patch(
                "https://api.notion.com/v1/pages/{}".format(page_id),
                json=data,
                headers={"Authorization": "Bearer " + token, "Notion-Version": "2022-06-28"},
            )
        except IndexError:
            print("结束")
            time.sleep(5)
            removeLine()
        else:
            num=num + 1
            if num < num4:
                print("num="+str(num))
                removeLine()
            if num == num4:
                try:
                    readDatabase(databaseId, headers)  # 下载notion-json
                    dict1=json.loads(json_file1)  # json to dict
                    print("转换成字典")
                    print(dict1)
                    num4=len(dict1.get('results'))
                    test1=dict1.get('results')[0]
                except IndexError:
                    print("已清空列表【最后确认】")
                else:
                    num=0
                    print("num4="+str(num4))
                    removeLine()



def removeLine_All():
    print("执行removeLine_All")
    global num, num4, token, databaseId, headers, json_file1, dict1
    readDatabase(databaseId, headers)  # 下载notion-json
    dict1=json.loads(json_file1)  # json to dict
    print("转换成字典")
    print(dict1)  # 打印dict
    num4=len(dict1.get('results'))
    removeLine()  # 删除每一行


def removePage(pageId, headers, databaseId, token):
    updateUrl=f"https://api.notion.com/v1/databases/{databaseId}"
    headers={
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token,
    }
    updateData={
        "properties": {
            "地区": {
                "multi_select": {
                    "options": [
                        {
                            "name": 'null'
                        },
                    ]
                }
            },
            "歌手": {
                "multi_select": {
                    "options": [
                        {
                            "name": 'null'
                        },
                    ]
                }
            },
            "歌词": {
                "multi_select": {
                    "options": [
                        {
                            "name": 'null'
                        },
                    ]
                }
            }

        }
    }

    data=json.dumps(updateData)
    print(str(data))

    response=requests.request("PATCH", updateUrl, headers=headers, data=data)
    print(response.status_code)
    print(response.text)


def createPage(databaseId, headers):
    print("运行createPage")
    global num1, lyric1, Name_format, music_tag_format1, music_tag_album, music_tag_year
    print(num1)
    createUrl='https://api.notion.com/v1/pages'

    newPageData={
        "parent": {"database_id": databaseId},
        "properties": {
            "ID": {
                "title": [
                    {
                        "text": {
                            "content": str(num1),
                        },
                    }
                ]
            },
            "地区": {
                "multi_select": [
                    {
                        "name": music_list[num1][5]
                    }
                ]
            },
            "歌手": {
                "multi_select": [
                    {
                        "name": str(f['artist'])
                    }
                ]
            },
            "歌曲": {
                "rich_text": [
                    {
                        "text": {
                            "content": str(f['title'])
                        }
                    }
                ]
            },
            "歌词": {
                "multi_select": [
                    {
                        "name": str(lyric1)
                    }
                ]
            },
            "命名格式": {
                "multi_select": [
                    {
                        "name": str(Name_format)
                    }
                ]
            },
            "专辑": {
                "multi_select": [
                    {
                        "name": music_tag_album
                    }
                ]
            },
            "年份": {
                "multi_select": [
                    {
                        "name": ".{}".format(music_tag_year)
                    }
                ]
            },
            "标签": {
                "multi_select": [
                    {
                        "name": music_tag_format1
                    }
                ]
            },
            "文件路径": {
                "rich_text": [
                    {
                        "text": {
                            "content": f"/{music_list[num1][-4]}/{music_list[num1][-3]}/{music_list[num1][-2]}/{music_list[num1][-1]}",
                        }
                    }
                ]
            },
            "守护者": {
                "multi_select": [
                    {
                        "name": "howard"
                    }
                ]
            }
        }
    }

    data=json.dumps(newPageData)
    print(str(data))
    res=requests.request("POST", createUrl, headers=headers, data=data)
    print(res.status_code)
    # print(res.text)


def updatePage(pageId, headers, GB_size):
    updateUrl=f"https://api.notion.com/v1/pages/{pageId}"

    updateData={
        "properties": {
            "ID": {
                "rich_text": [
                    {
                        "text": {
                            "content": GB_size
                        }
                    }
                ]
            }
        }
    }

    data=json.dumps(updateData)
    response=requests.request("PATCH", updateUrl, headers=headers, data=data)
    print(response.status_code)
    # print(response.text)


def music_tag_detection():
    try:
        print("运行识别标签music_tag_detection")
        global num1, lyric1, Name_format, f, music_tag_format1, music_tag_album, music_tag_year
        f=music_tag.load_file("{}".format(music_list_AP[num1]))
        music_info=str(f['artist']) + " - " + str(f['title'])
        music_info=music_info.replace("/", ";")
        if music_info in music_list[num1][-1]:
            music_tag_format1="正确"
        else:
            music_tag_format1="标签与文件名不对应"
        if str(f['album']) is not None:
            try:
                music_tag_album=str(f['album'])
            except Exception:
                print("album标签出错")
        else:
            music_tag_album="缺失"
        if str(f['year']) is not None:
            try:
                music_tag_year=str(f['year'])
            except Exception:
                print("year标签出错")
        else:
            music_tag_year="缺失"
    except Exception:
        print("错误继续")
    finally:
        print("-----")




def creatPage_ALL():
    print("运行creatPage_ALL")
    global num1, lyric1, Name_format, f, music_tag_format1, music_tag_album, music_tag_year
    # for num1 in range(len(music_list) - 1):
    print(music_list[num1])
    print(music_list_AP[num1])
    lyric1="无"
    if music_list[num1][music_artist] + " - " in music_list[num1][-1]:
        Name_format="正确"
    else:
        Name_format="不规范"
    if "flac" in music_list[num1][-1]:
        for i in range(len(music_list) - 1):
            t=music_list[i][-1].replace(".lrc", ".ok")
            if music_list[num1][-1].replace(".flac", ".ok") == t:
                lyric1="有"
        music_tag_detection()
        try:
            createPage(databaseId, headers)
        except Exception:
            print("重试")
            time.sleep(1)
            creatPage_ALL()

    elif "mp3" in music_list[num1][-1]:
        for i in range(len(music_list) - 1):
            t=music_list[i][-1].replace(".lrc", ".ok")
            if music_list[num1][-1].replace(".mp3", ".ok") == t:
                lyric1="有"
        music_tag_detection()
        try:
            createPage(databaseId, headers)
        except Exception:
            print("重试")
            time.sleep(1)
            creatPage_ALL()
    else:
        print("[非flac、mp3文件跳过]" + music_list[num1][-1])


# readDatabase(databaseId, headers)

# plex_music
# pageId='832b6bfc38e946af9ea15732dfdfdf29'
# updatePage(pageId, headers, GB_size)

# removePage(pageId, headers, databaseId, token)

removeLine_All()

find_music()
print(len(music_list))


num2=len(music_list) - 1
num1=0
while num1 < num2:
    creatPage_ALL()
    num1=num1 + 1



print("------------------------------")
print("------------------------------")
print("------------------------------")
print("------------------------------")
print("所有程序执行完成！！")