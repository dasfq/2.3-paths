import os, codecs

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':

    def find_text():
        dir = os.path.join(current_dir, migrations)
        files_list = list(os.listdir(dir))
        print(f'Всего файлов: {len(files_list)}')
        while True:
            files_sorted = []
            str = input('Введите строку: ')
            for file in files_list:
                with codecs.open(os.path.join(dir, file), "r", "utf_8_sig", errors='ignore') as f:
                    if str in f.read():
                        files_sorted.append(file)
            print(f'Отобрано файлов: {len(files_sorted)}')
            files_list = files_sorted.copy()

find_text()
