from test import data

user_id = 300
# print(data[user_id])
if user_id in data:
    print('Data ', data[user_id])
else:
    print('Invalid Key')

