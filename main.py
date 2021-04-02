import sqlite3
import os
import json
import time
import requests

# def get():
#     params = {
#         'text': 'name:1C',  # Текст фильтра. В имени должно быть слово "Аналитик"
#         'area': 1,  # Поиск ощуществляется по вакансиям города Москва
#         'page': page,  # Индекс страницы поиска на HH
#         'per_page': 100,  # Кол-во вакансий на 1 странице
#         'only_with_salary': True
#     }
#     req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
#     data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
#     req.close()
#     return data

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS vacancies(
#    id INT PRIMARY KEY,
#    name TEXT,
#    area TEXT,
#    salary_to INT,
#    salary_from INT);
# """)
# conn.commit()
#
# for page in range(0, 20):
#     # Преобразуем текст ответа запроса в справочник Python
#     d = json.loads(get())
#
#     # Сохраняем файлы в папку {путь до текущего документа со скриптом}\docs\pagination
#     # Определяем количество файлов в папке для сохранения документа с ответом запроса
#     # Полученное значение используем для формирования имени документа
#     nextFileName = 'C:/Users/lisik/PycharmProjects/pythonProject2/venv/Scripts/vacancies/{}.json'.format(len(os.listdir('C:/Users/lisik/PycharmProjects/pythonProject2/venv/Scripts/vacancies')))
#
#     # Создаем новый документ, записываем в него ответ запроса, после закрываем
#     f = open(nextFileName, mode='w', encoding='utf8')
#     f.write(json.dumps(d, ensure_ascii=False))
#     f.close()
#
#     for v in d['items']:
#         req = requests.get(v['url'])
#         data = req.content.decode(encoding='utf8')
#         req.close()
#
#         #Заполнение бд из файла страниц вакансиями
#         vacanciesy = v['id'], v['name'], v['area']['name'], v['salary']['to'], v['salary']['from']
#         area = v['area']['name']
#         name = v['name']
#         salary_to = v['salary']['to']
#         salary_from = v['salary']['from']
#         id = v['id']
#         cur.execute("INSERT INTO vacancies VALUES(?,?,?,?,?)", (id, name, area, salary_to, salary_from))
#         conn.commit()

# cur.execute("""
#   SELECT name, MIN ((salary_to+salary_from)/2)
#   FROM vacancies WHERE salary_to NOT like 'None' AND salary_from NOT like 'None';
# """)

# cur.execute("""
#   SELECT name, MAX ((salary_to+salary_from)/2)
#   FROM vacancies WHERE salary_to NOT like 'None' AND salary_from NOT like 'None';
# """)

cur.execute("""
  SELECT AVG ((salary_to+salary_from)/2)
  FROM vacancies WHERE salary_to NOT like 'None' AND salary_from NOT like 'None';
""")

# cur.execute("""
# SELECT COUNT (id)
# FROM vacancies
# """)

one_result = cur.fetchall()
print(one_result)

#     # Проверка на последнюю страницу, если вакансий меньше 2000
#     if (d['pages'] - page) <= 1:
#          break
#
#     # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать
#     time.sleep(0.25)
#
# print('Страницы поиска собраны')


