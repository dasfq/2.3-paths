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
            'v':'5.52'
        }
        r = requests.get(auth_url, auth_data)
        print('Линк для получения прав:\n', r.url )
        return r

    #делаем метод, который будет передавать запрос
    def send_request(self):
        r = requests.get(self.request_url + self.method, self.auth_data).json()
        return r
    # метод, в котором сначала формируем словарь группа:кол-ва участников, потом удаляем из неё группы, в которых есть друзья
    def get_groups(self):
    # returns json file with list of groups without any user's friends

        # get a list of ALL user's groups:
        self.request_url = 'https://api.vk.com/method/'
        self.method = 'groups.get'
        self.auth_data = {
            'user_id':171691064,
            'extended':1,
            'fields':'members_count',
            'access_token': self.token,
            'v':'5.52'
        }

        r = self.send_request()
        # r = requests.get(request_url+method, auth_data).json()
        groups_dict = {i['id']: i['members_count'] for i in r['response']['items']}
        print('Список групп:',groups_dict)

        # get a list of user's friends:
        self.method = 'friends.get'
        self.auth_data = {
            'user_id': 171691064,
            'access_token': self.token,
            'v': '5.52'
        }

        r = self.send_request()
        # r = requests.get(request_url+method, auth_data).json()
        friends_list = [i for i in r['response']['items']]

        # will delete groups with user's friends from the groups_list
        self.method = 'groups.isMember'
        for group_id, members_count in groups_dict.items():
            for friend in friends_list:
                self.auth_data = {
                    'group_id': group_id,
                    'user_id': friend,
                    'access_token': self.token,
                    'v': '5.52'
                }
                try:
                    r = self.send_request()
                    # r = requests.get(request_url+method,auth_data).json()
                    print('r равно:',r)
                    if r['response'] == 1:
                        groups_dict.pop(group_id)
                        break
                except KeyError:
                    # Make a pause 2 second due to error "too many requests per second"
                    time.sleep(2)
                    r = self.send_request()
                except RuntimeError:
                    #
                    r = self.send_request()

user1 = User(token = '6ec12f01485eaed78e2cdcf91d696e6531b7acb3976177e3132bb72fa469367a46333c59d4dd3d760cbde')
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
