import json

list_numbers = [1, 2, 3, 4, 5]
tuple_numbers = (6, 7, 8, 9)
json_data_1 = json.dumps(list_numbers)
json_data_2 = json.dumps(tuple_numbers)
print(json_data_1)
print(json_data_2)
print(type(json_data_1))
print('*' * 20)

dict_obj = {'b' : 80, 'a' : 25, 'c' : 60}
json_obj = json.dumps(dict_obj, sort_keys=True)
print(json_obj)