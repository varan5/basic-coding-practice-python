from database import Database as db
# record = {
#     'contact_no': '1234567890',
#     'first_name': 'Sam',
#     'last_name': 'Samuel',
#     'department': 'Sports',
#     'hobbies': ['cricket', 'chess', 'travel']
# }
# info.insert_one(record)

user_input = '1234567890'
data = info.find_one({ 'contact_no': user_input})
def find_result(data):
    hobbies_list = (data['hobbies'])
    counter = 1
    print('Your hobbies are: ')
    for hobby in hobbies_list:
        print(f'{counter}. {hobby}')
        counter += 1
    