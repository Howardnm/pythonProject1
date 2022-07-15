from dataclasses import replace
import music_tag
import os
import requests
import json
import time
import re


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