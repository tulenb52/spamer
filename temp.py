import json

with open('6285742280918.json') as f:
    data = json.load(f)

print(data['app_id'])