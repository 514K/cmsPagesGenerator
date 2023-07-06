enlst = []
lst = []

with open("links", "r", encoding="utf8") as f:
    for line in f:
          lst.append(line)
    f.close()

with open("enlinks", "r", encoding="utf8") as f2:
    for line in f2:
        enlst.append(line)
    f2.close()
print(lst)
print(enlst)

for i in range(len(lst)):
    with open("scoreLinks", "a+", encoding="utf8") as f:
        f.write(lst[i].replace("\n", "") + ";" + enlst[i])
    f.close()    