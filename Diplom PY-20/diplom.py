import requests
import json
import time


class User:
    def __init__(self, token):
        self.token = token
        self.app_id = 6788744
        self.auth_url = 'https://oauth.vk.com/authorize?'
        self.request_url = 'https://api.vk.com/method/'
        self.auth_data = {}
        self.method = ''
        self.user_id = 171691064
        self.version = '5.92'

    def get_link(self, app_id):
        """
        делаем ссылку для подтверждения прав доступа к нужным данным
        """
        self.auth_data = {
            'client_id': app_id,
            'display': 'page',
            'scope': 'friends,groups',
            'response_type': 'token',
            'v': self.version
        }
        r = requests.get(self.auth_url, self.auth_data)
        print('Линк для получения прав:\n', r.url)
        return

    def send_request(self):
        """
        делаем метод, который будет передавать запросы и проверять пришёл ли ответ без ошибок
        """
        r = requests.get(self.request_url + self.method, self.auth_data).json()
        if 'error' in r.keys():
            if r['error']['error_code'] == 6:
                time.sleep(0.2)
                self.send_request()
            else:
                print(r['error']['error_msg'])
                raise SystemExit
        print('.')
        print(r)
        return r

    def get_groups(self):
        """
        Составляем список отобранных групп:
            1. Найти словарь всех групп ЮЗЕРА.
            Нужно удалить из списка групп записи о деактивированных группах, чтобы дальше не было исключения KeyError.
            2. Найти список всех друзей Юзера.
            3. Проверяем по 100 друзей разом, входят ли они в группу пользователя. Перебираем всех друзей и все группы.
            4. Выводим словарь оставшихся групп.
        """
        self.method = 'groups.get'
        self.auth_data = {
            'user_id': self.user_id,
            'extended': 1,
            'fields': 'members_count',
            'access_token': self.token,
            'v': self.version
        }
        r = self.send_request()
        for a in r['response']['items']:
            if 'deactivated' in a.keys():
                r['response']['items'].remove(a)
        groups_dict = {i['id']: {'name': i['name'], 'members': i['members_count']} for i in r['response']['items']}
        """
        get a list of user's friends:
        """
        self.method = 'friends.get'
        self.auth_data = {
            'user_id': self.user_id,
            'access_token': self.token,
            'v': self.version
        }
        r = self.send_request()
        friends_list = [i for i in r['response']['items']]
        for group_id, group_data in groups_dict.copy().items():
            temp_list = friends_list.copy()
            friends_str = ''
            while len(temp_list) > 0:
                friends_list_100 = [temp_list.pop() for i in temp_list[:100] if len(temp_list) > 0]
                for i in friends_list_100:
                    friends_str = friends_str + str(i) + ','
                self.auth_data = {
                    'group_id': group_id,
                    'user_ids': friends_str,
                    'access_token': self.token,
                    'extended': '1',
                    'v': self.version
                }
                self.method = 'groups.isMember'
                r = self.send_request()
                for member_data in r['response']:
                    if member_data['member'] == 1:
                        groups_dict.pop(group_id)
                        break
                break
        with open('groups.json', 'w') as f:
            f.write(json.dumps(groups_dict))
        return groups_dict


if __name__ == '__main__':
    user1 = User(token='ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae')
    print('Список отобранных групп:\n', user1.get_groups())
