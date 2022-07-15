import os
import shutil
import time  # 引用时间函数

print("---------------------------------")
print("wiki指南：https://antique-hacksaw-c2a.notion.site/Plex-music-family-029133efa133486db0c3624e4c5521de")

print("请确保音乐文件通过MusicTag规范化，不懂操作请看wiki指南：MusicTag第四步骤")
print("例子：")
print("周杰伦 - 爱的飞行日记.flac")
print("张艺兴 - 爱的引力.flac")
print("---------------------------------")
print("音乐文件名是否已经规范化处理？")
txt1 = input("回车确认：")
print("  ")
print("  ")
print("---------------------------------")
print("请输入音乐文件夹绝对路径（在本窗口里右键，即可粘贴内容）")
print("例如：C:\\"+"\\Users\85099\Desktop\我的歌单")
print("例如：\\"+"\\192.168.1.20\downloads\音乐\我的歌单")
path = input("请输入：")
# 去cmd构建exe："pyinstaller -i 456.ico -F C:\Users\85099\PycharmProjects\pythonProject1\notion\music_sort.py"
# path = "C:\\Users\85099\Desktop\新建文件夹"
# 获取所有文件
for filename in os.listdir(path):
    time.sleep(0.05)  # 每个回合等待0.08秒
    findPath = os.path.join(path, filename)
    if(os.path.isfile(findPath)):
        # print(findPath)
        # 分析出歌手和歌名
        try:
            filenameArr = filename.split(' - ')
            # 开始构造
            # 检查歌手文件夹是否存在，不存在就创建，并且移动该文件到此目录
            # 检查文件夹目录
            dstdir=os.path.join(path, filenameArr[0])
            if (os.path.exists(dstdir) is False):
                # 不存在，创建！
                os.mkdir(dstdir)
            # 移动歌曲
            shutil.move(findPath, os.path.join(dstdir, filename))
        except IOError:
            print('【歌曲命名错误】：'+findPath)
            continue

    print(filename+' 完成分类!')

input("-----按enter，即可关闭窗口-----")

