import json

flist = []
rlist = []
fdict = {}
with open("text_task47.txt", 'r', 1, 'utf8') as efile:
    for line in efile:
        a = line.split()
        if float(a[2]) - float(a[3]) > 0:
            rlist.append(float(a[2]) - float(a[3]))
        fdict.setdefault(a[0], float(a[2]) - float(a[3]))
    flist.append(fdict)
    flist.append({"AVG revenue": sum(rlist) / len(rlist)})

print(flist)
with open("json_task47.json", 'w') as jfile:
    json.dump(flist, jfile, indent=4)
