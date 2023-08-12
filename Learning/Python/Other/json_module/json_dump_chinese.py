import json

obj_list = [
    {"日本" : "Japan", "首都" : "Tokyo"},
    {"美國" : "USA", "首都" : "Washington"}
]
fn = 'output.json'
with open(fn, 'w', encoding='utf-8') as fn_obj:
    json.dump(obj_list, fn_obj, ensure_ascii=False, indent=2)