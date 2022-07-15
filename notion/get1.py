import os
import requests
import json
import time
# pip3 install requests





token='secret_DkYKff6IQJdGJTqgFslKQqGpLtsu44RiH3Vsa2nhYjO'

databaseId='b2716edc91ae46398d45a4efb376efee'

headers={
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

GB_size=""

# 检索文件夹大小

def osos(folder_path):
    full_size = sum(sum(os.path.getsize(os.path.join(parent, file)) for file in files) for parent, dirs, files in os.walk(folder_path))
    global GB_size
    GB_size="%.2f GB" % (full_size / 1024 / 1024 / 1024)
    print("%.2f GB" % (full_size/1024/1024/1024))


# notion

def readDatabase(databaseId, headers):
    readUrl=f"https://api.notion.com/v1/databases/{databaseId}/query"

    res=requests.request("POST", readUrl, headers=headers)
    data=res.json()
    print(res.status_code)
    print(res.text)

    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


def updatePage(pageId, headers, GB_size):
    updateUrl=f"https://api.notion.com/v1/pages/{pageId}"

    updateData={
        "properties": {
            "存量": {
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
pageId='7bc7a9b5-5580-469a-a188-34fecc12547a'
osos("/volume1/Resilio Sync/folders/plex_music")
updatePage(pageId, headers, GB_size)

# plex_music候选
pageId='ce1ed8cb-993c-4955-b847-6e48bc77d53a'
osos("/volume1/Resilio Sync/folders/plex_music候选区")
updatePage(pageId, headers, GB_size)

# 更新时间
pageId='4e403edf-6582-4ca7-a40a-8184354835e2'
today=time.strftime("%Y/%m/%d %H:%M", time.localtime())
updatePage(pageId, headers, today)