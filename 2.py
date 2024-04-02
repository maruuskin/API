import csv
import json

cnt = 0
ans = []
dict = {}
sett = set()
with open('battles.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=':', quotechar='"')
    for index, row in enumerate(reader):
        if index != 0:
            if row[4] == '1':
                dict[row[2]] = dict.get(row[2], 0) + int(row[3])
                sett.add(row[2])
sett = sorted(list(sett))
for i in sett:
    key = i
    val = dict[i]
    sl = {
        "monster": key,
        "success": val
    }
    ans.append(sl)
with open('fights.json', 'w') as f:
    json.dump(ans, f, indent=4)
