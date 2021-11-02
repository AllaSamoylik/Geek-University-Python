from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as f_users:
    with open('hobby.csv', 'r', encoding='utf-8') as f_hobby:
        with open('users_hobby.json', 'w', encoding='utf-8') as f_sum:
            users = f_users.read().splitlines()
            hobby = f_hobby.read().splitlines()

            if len(users) >= len(hobby):
                users_hobby = dict(zip_longest(users, hobby))
                json.dump(users_hobby, f_sum)
            else:
                print('1')

with open('users_hobby.json', 'r', encoding='utf-8') as f_sum:
    users_hobby = json.load(f_sum)
    print(users_hobby)
