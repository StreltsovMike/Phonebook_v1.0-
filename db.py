import sqlite3
import openpyxl as op

# def read_xlsx():   # Выдает список с значениями каждой ячейки из phoonebook.xlsx
#     data = op.open('phonebook.xlsx', read_only=True)
#     sheet = data.active
#     data_list = []
#     for row in range(2, (sheet.max_row + 1)):
#         for col in range(1,5):
#             data_list.append(sheet[row][col].value)
#     cortej_list = []
#     for i in range(0, len(data_list), 4):
#         p = (data_list[i], data_list[i+1], int(data_list[i+2]), data_list[i+3])
#         cortej_list.append(p)
#     return cortej_list

def add_contact(person):
    db = sqlite3.connect('phonebook.db')
    curs = db.cursor()
    curs.execute("INSERT INTO phonebook (name, surname, phone, description) VALUES (?, ?, ?, ?)", person)
    db.commit()
    db.close()

def delete_contact(id):
    db = sqlite3.connect('phonebook.db')
    curs = db.cursor()
    curs.execute("DELETE FROM phonebook WHERE userid = ?", (id,))
    db.commit()
    db.close()

def find_contact(name):
    db = sqlite3.connect('phonebook.db')
    curs = db.cursor()
    curs.execute("SELECT * FROM phonebook WHERE name = ?", (name,))
    finded = curs.fetchall()
    db.close()
    return finded


# x = read_xlsx()
# db = sqlite3.connect('phonebook.db')
# curs = db.cursor()
# curs.execute("""CREATE TABLE IF NOT EXISTS phonebook(
#    userid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#    name TEXT,
#    surname TEXT,
#    phone number INT,
#    description TEXT);
# """)
# person = ('Lucas', 'Skywalker', 89109156633, 'job')
# for i in range(len(x)):
#     person = x[i]
#     curs.execute("INSERT INTO phonebook (name, surname, phone, description) VALUES (?, ?, ?, ?)", person)
#     db.commit()
# curs.execute("SELECT * FROM phonebook")
# p = curs.fetchmany(10)
# print(p)

# db.close()

# name = str('bob')
# p = find_contact(name)
# print(p)
