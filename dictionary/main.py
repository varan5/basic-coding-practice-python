from test import data

user_input_id = 200
todo_list = data[user_input_id]
counter = 0
for todo in todo_list:
    counter += 1
    print(f'{counter}. {todo}')