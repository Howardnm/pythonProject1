import urllib.request
import urllib.parse
import json

# 网易云音乐


# qq音乐
# url='https://api.qq.jsososo.com/songlist?id=4213000588'
url='http://howard115.synology.me:54008/songlist?id=3569246889'

# 正常的方式进行访问
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
request=urllib.request.Request(url=url, headers=headers)
response=urllib.request.urlopen(request)
# 输出所有
# print(response.read().decode('utf8'))
ls=response.read().decode('utf8')
ls=str(ls)
# 将内容写入文件中
fo1=open("songlist.json", "w", encoding='utf8')
fo1.write(ls)
fo1.close()

# 读取json文件，并json转成py字典格式
with open('songlist.json', 'r', encoding='utf8')as fp:
    json_data=json.load(fp)
# print(json_data)

# get检索键，并输出该值到result1列表
# json_data = response.read().decode('utf8')
data=json_data.get("data").get("songlist")  # 字典存在套娃
result1=[]
for i in data:
    result1.append(i.get("songname"))
print(result1)

# 输出result1列表到qq123.txt
fo=open("songlist-songname.txt", "w", encoding='utf8')
for line in result1:
    fo.write(line + '\n')
fo.close()
