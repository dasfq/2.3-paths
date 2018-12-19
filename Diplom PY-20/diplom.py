# 1. Найти словарь всех групп ЮЗЕРА (id: кол-во участников)
# 2. Найти список всех друзей Юзера
# 3.
# 3.1. Берём первую группу.
# 3.2. Берём первых 500 друзей, проверяем методом group.isMember есть ли среди этих друзей состоящие в данной группе.
# 3.3. Берём вторых и третьх 500 друзей, пока не закончатся друзья, и проверяем с тем же id группы.
# 4. Если находим хоть одного друга в группе, то удаляем этот id группы из словаря.
# 5. Перебираем остальные группы аналогично.
# 6. Выводим словарь оставшихся групп.


import requests, pprint, json, time

class User:
    def __init__(self, token):
        self.token = token

    # делаем ссылку для подтверждения прав доступа к нужным данным
    def get_link(app_id):
        app_id = 6788744
        auth_url = 'https://oauth.vk.com/authorize?'
        auth_data = {
            'client_id':app_id,
            'display':'page',
            'scope':'friends,groups',
            'response_type':'token',
            'v':'5.92'
        }
        r = requests.get(auth_url, auth_data)
        print('Линк для получения прав:\n', r.url )
        return

    #делаем метод, который будет передавать запрос
    def send_request(self):
        r = requests.get(self.request_url + self.method, self.auth_data).json()
        return r

    def get_groups(self):
        # get a dict of ALL user's groups:
        self.request_url = 'https://api.vk.com/method/'
        self.method = 'groups.get'
        self.auth_data = {
            'user_id':171691064,
            'extended':1,
            'fields':'members_count',
            'access_token': self.token,
            'v':'5.92'
        }
        r = self.send_request()
        groups_dict = {i['id']: i['members_count'] for i in r['response']['items']}
        print('Список всех групп:',groups_dict)

        # get a list of user's friends:
        self.method = 'friends.get'
        self.auth_data = {
            'user_id': 171691064,
            'access_token': self.token,
            'v': '5.92'
        }
        r = self.send_request()
        friends_list = [i for i in r['response']['items']]

        # will delete groups with user's friends from the groups_list
        for group_id, members_count in groups_dict.copy().items():
            temp_list = friends_list.copy()
            while len(temp_list) > 0:
                friends_list_500 = [temp_list.pop() for i in temp_list[:500] if len(temp_list)>0]
                # print('list of 500 friends:\n', friends_list_500)
                self.auth_data = {
                    'group_id': group_id,
                    'user_ids': friends_list_500,
                    'access_token': self.token,
                    'extended': '1',
                    'v': '5.52'
                }
                self.method = 'groups.isMember'
                r = self.send_request()
                time.sleep(0.2)
                print('r равно:',r)

                # Удаляем id группы из словаря, если находим друга в группе
                for member_data in r['response']:
                    if member_data['member'] = 1:
                        groups_dict.pop(group_id)
                        break

user1 = User(token = '2ac36695da521d2f3b8498bfe806a24735a1d7ce19f1b2d19ff35ccc2ece3e4836ea8ab7ad5a1a8e8577f')
print(user1.get_groups())


# [
#     {
#     “name”: “Название группы”,
#     “gid”: “идентификатор группы”,
#     “members_count”: количество_участников_сообщества
#     },
#     {
#     …
#     }
# ]
