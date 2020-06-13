import json

f = open('olddb.json',)

data = json.load(f)

new = {"internet":[], "velocity":[], "searchVirality":[], "demographic":[], "emerging":[]}
seen = []

for obj in data:
    if (obj["type"] == "Demographic"):
        new["demographic"].append(obj)
    elif (obj["type"] == "Velocity"):
        new["velocity"].append(obj)
    elif (obj["type"] == "Search Virality"):
        new["searchVirality"].append(obj)
    elif (obj["type"] == "Internet/TikTok"):
        new["internet"].append(obj)
    elif (obj["type"] == "Emerging Artists"):
        new["emerging"].append(obj)


print(json.dumps(new))

with open('db.json', 'w', encoding='utf-8') as f:
    json.dump(new, f, indent=4)
