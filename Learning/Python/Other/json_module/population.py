import json

fn = 'populations.json'
with open(fn) as fn_obj:
    get_datas = json.load(fn_obj)

for get_data in get_datas:
    if get_data["Year"] == '2000':
        country_name = get_data["Country Name"]
        country_code = get_data["Country Code"]
        population = int(float(get_data["Numbers"]))
        print('-' * 30)
        print(f'Country Name : {country_name}')
        print(f'Country Code : {country_code}')
        print(f'Populations : {population}')