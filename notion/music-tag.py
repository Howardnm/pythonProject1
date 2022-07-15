import music_tag


f = music_tag.load_file("C:\\Users\85099\Desktop\新建文件夹\队长 - 夜行.flac")

# dict access returns a MetadataItem
print(f['title'])
print(f['artist'])
print(f['album'])
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