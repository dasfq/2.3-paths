import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':

    def find_text():
        files_sorted = []
        str = input('Введите строку: ')
        dir = os.path.join(current_dir, migrations)
        files_list = list(os.listdir(dir))
        print(files_list[0:4])
        print(f'Всего файлов: {len(files_list)}')
        for file in files_list:
            with open(os.path.join(dir,file)) as f:
                if str in f:
                    files_sorted.append(file)


    pass

find_text()
