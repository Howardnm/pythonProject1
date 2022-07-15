fo=open("/volume1/Resilio Sync/folders/foo.txt")
t=fo.read()
fo.close()
print(t)
fo = open("/volume1/Resilio Sync/folders/foo.txt", "r")
music_list_AP = []
for line in fo:
    line = line.replace("\n","")
    music_list_AP.append(line)
fo.close()
print("----------------")
print(music_list_AP)