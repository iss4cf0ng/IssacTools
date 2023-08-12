import json

obj = {
    "Asia":[
        {"Japan" : "Tokyo"},
        {"China" : "Beijing"}
    ]
}
fn = 'output.json'
with open(fn, 'w') as fn_obj:
    json.dump(obj, fn_obj)