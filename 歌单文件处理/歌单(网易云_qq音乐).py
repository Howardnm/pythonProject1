# python 3
import urllib.request
import urllib.parse
import json
import socket


# 域名解析
def urlsearch():
    try:
        result=socket.getaddrinfo("howard1115.synology.me", None)
        result=result[0][4][0]
        return result
    except:
        try:
            result=socket.getaddrinfo("howard115.zicp.net", None)
            result=result[0][4][0]
            return result
        except:
            print("服务器API无法访问")


chose=input("网易云输入1，qq音乐输入2：")
if chose == "1":
    # 网易云音乐
    print("例如：https://music.163.com/#/playlist?id=3168324249，输入：3168324249")
    uid=input("输入：")
    url='http://' + urlsearch() + ':3000/playlist/detail?id=' + uid
    get1, get2, get3="playlist", "tracks", "name"
    get4, get5="ar", "name"
    print("处理中..")
elif chose == "2":
    # qq音乐
    print("例如：https://y.qq.com/n/yqq/playlist/3569246889.html，输入：3569246889")
    uid=input("输入：")
    url='https://api.qq.jsososo.com/songlist?id=' + uid
    # url = 'http://howard115.synology.me:54008/songlist?id=3569246889' + uid
    get1, get2, get3="data", "songlist", "songname"
    get4, get5="singer", "name"
    print("处理中..")
else:
    print("输入错误")

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
request=urllib.request.Request(url=url, headers=headers)
response=urllib.request.urlopen(request)
# 输出所有
# print(response.read().decode('utf8'))
ls=response.read().decode('utf8')

# 将内容写入文件中
fo1=open("songlist.json", "w", encoding='utf8')
fo1.write(ls)
fo1.close()

# 读取json文件，并json转成py字典格式
# 方法1：
# with open('songlist.json', 'r', encoding='utf8')as fp:
#    json_data=json.load(fp)
# print(json_data)
# 方法2：
json_data=json.loads(ls)

# get检索键，并输出该值到result1列表
data=json_data.get(get1).get(get2)  # 字典存在套娃
# print(data)
result1=[]
for i in data:
    result1.append(eval('i.get(get3) + " - " + i.get(get4)[0].get(get5)'))  # 歌名+演唱者

# print(result1)

# 输出result1列表到songlist-songname.txt
fo=open("songlist-songname.txt", "w", encoding='utf8')
for line in result1:
    fo.write(line + '\n')
fo.close()

# 打印在终端
fo2=open("songlist-songname.txt", "r", encoding='utf8')
for line in fo2.readlines():
    print(line, end="")
fo2.close()

print("")
print("歌单已导出到：songlist-songname.txt")
# input("-----按enter，即可关闭窗口-----")
