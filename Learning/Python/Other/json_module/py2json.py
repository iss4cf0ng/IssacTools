import json

obj = '{"Asia":\
    [{"Japen":"Tokyo"},\
    {"China":"Beijing"}]\
    }'
json_obj = json.loads(obj)
print(json_obj)
print(json_obj["Asia"])
print(json_obj["Asia"][0])
print(json_obj["Asia"][1])
print(json_obj["Asia"][0]["Japen"])
print(json_obj["Asia"][1]["China"])