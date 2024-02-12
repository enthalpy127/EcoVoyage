import shelve
from Order import Orders
# with shelve.open('order_data', 'c') as db:
#     orderid_list = []
#     for i in db:
#         orderid_list.append(i)
#     orderid_list.sort()
#     orderid = int(orderid_list[-1]) + 1
#     dictte = {}
#     dictte['order_id'] = orderid
#     for i in list(data):
#         dictte[i] = data[i]
#
#     print(dictte)
#     print(orderid)

print(Orders.calculate_price("Similan Islands", 5,0))


# Show what is stored in shelve
# with shelve.open('order_data', 'c') as db:
#     for i in db:
#         print(f"{i}, {db[i]}")
#         # print(db[i]['destination'])
#     # print(f"{Orders.calculate_price(db[i]['destination'], int(db[i]['adults']), int(db[i]['children']))}")
#     key_names = ["adult_price", "children_price", "total amount"]
#     num = 0
#     for i in Orders.calculate_price(db[i]['destination'], int(db[i]['adults']), int(db[i]['children'])):
#         print(f'{key_names[num]} : {i}')
#         num += 1

# with shelve.open('order_data', 'c') as db:
#     dictti = {'order_id': 1, 'firstname': 'fsdfd', 'lastname': 'sdfds', 'email': 'sdfsfd@dfgfdg', 'phone': '12345678', 'airport': 'rsfvuygi', 'destination': 'Mount Rigi', 'departure': '2024-02-20', 'adults': '9', 'children': '10', 'cardnumber': '123412341234', 'cardholder': 'dscy', 'cardexpiry': '05/05', 'cardsec': '777', 'adult_price': '400', 'children_price': '320', 'total_amount': '6800', 'Refunded': 'F'}
#     print(dictti['order_id'])
#     db[str(dictti['order_id'])] = dictti
#     for i in db.values():
#         dictti = {}
#         i['Refunded'] = 'F'
#         dictti[i['order_id']] = i
#         print(f'{dictti}')

#Printing Database
with shelve.open('order_data', 'r') as db:
    for i in db:
        for a in i:
            print(a, type(a))

# with shelve.open('order_data', 'c') as db:
#     id = 3
#
#     if id in db:
#         for i in db:  # Indentation fixed
#             print(f'{type(i)}, {db[i]}')
#     else:
#         print(f"Key '{id}' not found in the shelve.")
#
#     try:
#         for i in db:  # Indentation fixed
#             print(f'{type(i)}, {db[i]}')
#     except KeyError as e:
#         print(f"KeyError: {e}")

with shelve.open('order_data', 'c') as db:
    # id = str(3)
    # db.pop(id)
    for i in db:
        print(f'{type(i)}, {db[i]}')