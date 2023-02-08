import sqlite3
import os
conn = sqlite3.connect("baza_podobina.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS telephone_book5
                 (surname TEXT,
                 name TEXT,
                 patronymic TEXT,
                 number_phone INTEGER)
               """)
print('введите количество строк, которые хотите добавить: ')
kol_string = int(input())
for kol_string in range(1, kol_string+1):
    surname = 'surname' + str(kol_string)
    name = 'name' + str(kol_string)
    patronymic = 'patronymic' + str(kol_string)
    number = 'number' + str(kol_string)
    print('введите фамилию: ')
    surname = str(input())
    print('введите имя: ')
    name = str(input())
    print('введите отчество: ')
    patronymic = str(input())
    print('введите номер телефона: ')
    number = str(input())
    users = [surname, name, patronymic, number]
    conn.commit()
    cursor.execute("INSERT INTO telephone_book5 VALUES(?, ?, ?, ?);", users)
    conn.commit()
print('открываю базу данных...')
os.startfile(r'C:\Program Files\SQLiteStudio\SQLiteStudio.exe')

