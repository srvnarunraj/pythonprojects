import json

obj = {"Filename" : "Home Assignment"}
with open ('sample.txt', 'w') as doc:
    json.dump(obj,doc)


with open('sample.txt', 'r') as f:
    data = json.load(f)
    print(f)