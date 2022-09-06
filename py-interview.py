from pprint import pprint as pp
# dicts
first_orders = [
{"date": "2021-08-03 03:37:52", "item_id": 'cd63d5a8-bfba-4082-9f85-b8aa039ae9ba'},
{"date": "2021-08-10 09:21:18", "item_id": '19b5b16b-04ac-43d0-87dc-b2a09946dfcd'},
{"date": "2021-09-01 07:16:02", "item_id": '3c74323f-382b-487e-b8bd-2495ecb79ef0'},]

second_orders = [
{"date": "2029-11-20 19:01:03", "item_id": '3c74323f-382b-487e-b8bd-2495ecb79ef0'},
{"date": "2021-08-03 03:37:52", "item_id": '264e3b54-94aa-4447-9bef-295907b4a259'},
{"date": "2021-08-10 09:21:18", "item_id": '3c74323f-382b-487e-b8bd-2495ecb79ef0'},
{"date": "2021-09-01 07:16:02", "item_id": '4f9e3710-61c3-4f74-aa7b-e0100b815eaa'},]

# concatenate
l3 = first_orders + second_orders
# pp(l3)

# ordenar
l3.sort(key=lambda x:x['date'], reverse=True)
for i in l3:
    print(i)


# sin id repetidos
ids = []
uniques = []

for i in l3:
    if(i['item_id'] not in ids):
        ids.append(i['item_id'])
        uniques.append(i)


print("-"*100)
for i in uniques:
    print(i)

# el maximo
max_date = uniques[0]
print(f"el maximo es: {max_date}")
