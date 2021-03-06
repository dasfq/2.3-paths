import xml.etree.ElementTree as Etree
import time

class Timer():
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time()
        self.interval = self.stop - self.start
        print(f'Старт: {time.ctime(self.start)}, Остановка: {time.ctime(self.stop)}, Порачено времени: {self.interval}')
        return False


def get_words_list():
    parser = Etree.XMLParser(encoding='utf-8')
    tree = Etree.parse("files/newsafr.xml", parser)
    root = tree.getroot()
    words_list = []
    for i in root[0]:
        if i.tag == "item":
            words_list.extend((filter(lambda x: len(x) > 6, i[2].text.split())))
    # print(words_list)
    return(words_list)



def get_frequent():
    words_list = get_words_list()
    words_dict = {}
    for i in words_list:
        words_dict[i] = words_list.count(i)
    top_10_list = sorted(words_dict.items(), key = lambda item:item[1], reverse=True)
    print(top_10_list[0:10])

with Timer():
    get_frequent()