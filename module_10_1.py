
from threading import Thread
import time
from datetime import datetime
from time import sleep

def write_words(word_count, file_name):
    with open(file_name,'w',encoding='utf8')as file:
        for line in range(1,word_count+1):
            file.write(f'Какое-то слово № {str(line)}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потока {time_res}\n')

time_start = datetime.now()
trd_1 = Thread(target=write_words, args=(10, 'example5.txt'))
trd_2 = Thread(target=write_words, args=(30, 'example6.txt'))
trd_3 = Thread(target=write_words, args=(200, 'example7.txt'))
trd_4 = Thread(target=write_words, args=(100, 'example8.txt'))

trd_1.start()
trd_2.start()
trd_3.start()
trd_4.start()

trd_1.join()
trd_2.join()
trd_3.join()
trd_4.join()
time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потока {time_res}')
