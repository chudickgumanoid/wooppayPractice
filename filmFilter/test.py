import pandas as pd
import flask
import sqlalchemy

name = input("Введите своё имя: ")
print("Привет, " + name)


df=pd.read_csv('netflix.csv')
print(df)

df=pd.read_csv('netflix.csv')
article_read[article_read.source == 'type']
print(df)

'''
# Сброс ограничений на количество выводимых рядов
pandas.set_option('display.max_rows', None)
# Сброс ограничений на число столбцов
pandas.set_option('display.max_columns', None)
'''
#print(df)
'''
import csv
# открываем файлик и указываем нужную кодировку
with open("netflix.csv", encoding='utf-8') as r_file:
    # cоздаем объект reader, символ-разделитель ","
    file_reader = csv.DictReader(r_file, delimiter = ",")
    # cчетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # Вывод строк
            print(f'    {row["show_id"]} это айди - {row["type"]} а это type')
        count += 1
    print(f'Всего в файле {count} строк.')
    '''