from concurrent.futures import ThreadPoolExecutor
import threading
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
    "Notion-Version": "2021-05-13"
}

music_list=[]
GB_size=""
json_file1=""
num=0


# 创建一个包含2条线程的线程池
pool = ThreadPoolExecutor(max_workers=2)



# 遍历本地音乐文件
def find_music():
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
                # print(os.path.join(filepath, fi_d))
                ppp=os.path.join(filepath, fi_d)
                list1.append(ppp)
                # print(list1)

    # 递归遍历/root目录下所有文件
    gci('/volume1/Resilio Sync/folders/plex_music')

    # 遍历后的绝对路径，写入txt
    fo=open("/volume1/Resilio Sync/folders/foo.txt", "w+", encoding='utf8')
    for line in list1:
        fo.writelines(line + "\n")
    fo.close()
    # print(list1)

    # 删除包含".sync"的行
    list2=[]
    matchPattern=re.compile(r'.sync')
    file=open('/volume1/Resilio Sync/folders/foo.txt', 'r')
    while 1:
        line=file.readline()
        if not line:
            print("Read file End or Error")
            break
        elif matchPattern.search(line):
            pass
        else:
            list2.append(line)
    file.close()
    file=open(r'/volume1/Resilio Sync/folders/foo.txt', 'w')
    for i in list2:
        file.write(i)
    file.close()

    # 读取绝对路径，识别"/"，将列表内元素细分，形成套娃列表
    fo=open("/volume1/Resilio Sync/folders/foo.txt", "r")
    for line in fo:
        line=line.replace("\n", "")
        music_list.append(line.split("/"))
    # print(music_list)
    fo.close()
    # 整理后的列表重新写入
    fo=open("/volume1/Resilio Sync/folders/foo1.txt", "w+", encoding='utf8')
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
    print(json_file1)
    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)

def removePATCH(page_id, data):
    requests.patch(
        "https://api.notion.com/v1/pages/{}".format(page_id),
        json=data,
        headers={"Authorization": "Bearer " + token, "Notion-Version": "2021-05-13"},
    )
# 下载notion-json，提取每一行的id
def removeLine():
    print("执行removeLine")
    global num
    global token
    global page_id
    global data
    try:
        test1=dict1.get('results')[0]
    except IndexError:
        print("已清空列表")
    else:
        try:
            data={'archived': True}
            page_id=dict1.get('results')[num].get('id')  # "提取每一行id"
            print(dict1.get('results')[num].get('id'))
            removePATCH(page_id, data)

        except IndexError:
            print("结束")
            time.sleep(0.5)
            removeLine_All()

def removeLine_thead():
    global num
    try:
        # 向线程池提交一个task, 50会作为action()函数的参数
        future1=pool.submit(removeLine)
        num=num + 1
        future2=pool.submit(removeLine)
        num=num + 1
        # 判断future1代表的任务是否结束
        print(future1.done())
        # 判断future2代表的任务是否结束
        print(future2.done())
        # 查看future1代表的任务返回的结果
        removeLine()  # 删除每一行
    except:
        print()

def removeLine_All():
    print("执行removeLine_All")
    global dict1
    readDatabase(databaseId, headers)  # 下载notion-json
    dict1=json.loads(json_file1)  # json to dict
    print(dict1)  # 打印dict
    removeLine_thead()


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


def createPage(databaseId, headers, num1, lyric1, Name_format):
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
                        "name": music_list[num1][6]
                    }
                ]
            },
            "歌曲": {
                "rich_text": [
                    {
                        "text": {
                            "content": music_list[num1][-1]
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


# readDatabase(databaseId, headers)

# plex_music
# pageId='832b6bfc38e946af9ea15732dfdfdf29'
# updatePage(pageId, headers, GB_size)

# removePage(pageId, headers, databaseId, token)

removeLine_All()

find_music()
print(len(music_list))

for num1 in range(len(music_list) - 1):
    lyric1="无"
    Name_format="不规范"
    if music_list[num1][6]+" - " in music_list[num1][-1]:
        Name_format="正确"
    if "flac" in music_list[num1][-1]:
        for i in range(len(music_list) - 1):
            t=music_list[i][-1].replace(".lrc", ".flac")
            if music_list[num1][-1] == t:
                lyric1="有"
        createPage(databaseId, headers, num1, lyric1, Name_format)
    elif "mp3" in music_list[num1][-1]:
        for i in range(len(music_list) - 1):
            t=music_list[i][-1].replace(".lrc", ".mp3")
            if music_list[num1][-1] == t:
                lyric1="有"
        createPage(databaseId, headers, num1, lyric1, Name_format)
    else:
        print("[非flac、mp3文件跳过]" + music_list[num1][-1])

# for num1 in range(len(music_list) - 1):
#     lyric1="无"
#     music_lyric1=music_list[num1][-1].replace(".flac" and ".mp3", ".ok") # 限制格式上传
#     if ".ok" in music_lyric1:
#         for i in range(len(music_list) - 1):
#             t=music_list[i][-1].replace(".flac" and ".mp3", ".lrc")
#             if music_list[num1][-1] == t:
#                 lyric1="有"
#         createPage(databaseId, headers, num1, lyric1)
#     else:
#         print("[非flac、mp3文件跳过]" + music_list[num1][-1])
