import os
import requests
import json
import time
import re

json_file1=""

token='secret_DkYKff6IQJdGJTqgFslKQqGpLtsu44RiH3Vsa2nhYjO'

databaseId='8b7919e4ec944391a82fa0a80a8e7212'

headers={
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

num=0


# 下载notion-json
def readDatabase(databaseId, headers):
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


# 下载notion-json，提取每一行的id
def removeLine():
    global num
    global token
    try:
        data={'archived': True}
        page_id=dict1.get('results')[num].get('id')  # "每一行id"
        print(dict1.get('results')[num].get('id'))
        requests.patch(
            "https://api.notion.com/v1/pages/{}".format(page_id),
            json=data,
            headers={"Authorization": "Bearer " + token, "Notion-Version": "2021-05-13"},
        )
    except IOError:
        print("结束")
    else:
        num=num + 1
        removeLine()


def removeLine_All():
    global dict1
    global json_file1
    readDatabase(databaseId, headers)  # 下载notion-json
    dict1=json.loads(json_file1)  # json to dict
    print(dict1)  # 打印dict
    removeLine()  # 删除每一行


removeLine_All()
