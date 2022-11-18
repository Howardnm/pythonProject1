import music_tag


f = music_tag.load_file("C:\\Users\85099\Desktop\新建文件夹\队长 - 夜行.flac")

# dict access returns a MetadataItem
print(f['title']) # 艺术家
print(f['artist']) # 歌手
print(f['album']) # 专辑
print(f['tracknumber']) # 轨道号
print(f['discnumber']) # 蝶号
print(f['albumartist']) # 专辑艺术家
print(f['compilation'])
print(f['totaltracks'])
print(f['artwork']) # 封面




try:
    print(f['year'])
except BaseException:
    print("错误继续")
finally:
    print("-----")


# title_item = f['title']

# MetadataItems keep track of multi-valued keys
# title_item.values  # -> ['440Hz']

# A single value can be extracted
# title_item.first  # -> '440Hz'
# title_item.value  # -> '440Hz'

# MetadataItems can also be cast to a string
# str(title_item)  # -> '440Hz'