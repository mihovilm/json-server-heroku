import json

f = open('olddb.json',)

data = json.load(f)

new = {"internet":[], "velocity":[], "searchVirality":[], "demographic":[], "emerging":[]}
seenTracks = {"internet":[], "velocity":[], "searchVirality":[], "demographic":[], "emerging":[]}

for obj in data:
    if (obj["type"] == "Demographic"):
        if (obj["track_name"] not in seenTracks["demographic"]):
            new["demographic"].append(obj)
            seenTracks["demographic"].append(obj["track_name"])
    elif (obj["type"] == "Velocity"):
        if (obj["track_name"] not in seenTracks["velocity"]):
            new["velocity"].append(obj)
            seenTracks["velocity"].append(obj["track_name"])
    elif (obj["type"] == "Search Virality"):
        if (obj["track_name"] not in seenTracks["searchVirality"]):
            new["searchVirality"].append(obj)
            seenTracks["searchVirality"].append(obj["track_name"])
    elif (obj["type"] == "Internet/TikTok"):
        if (obj["track_name"] not in seenTracks["internet"]):
            new["internet"].append(obj)
            seenTracks["internet"].append(obj["track_name"])
    elif (obj["type"] == "Emerging Artists"):
        if (obj["track_name"] not in seenTracks["emerging"]):
            new["emerging"].append(obj)
            seenTracks["emerging"].append(obj["track_name"])

print(json.dumps(new))

with open('db.json', 'w', encoding='utf-8') as f:
    json.dump(new, f, indent=4)
