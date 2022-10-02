from tkinter import *
import db


def add_contact():
    global entry_name, entry_last_name, entry_phone_number, entry_description
    label_instruction.config(text='Введите данные контакта:')
    label_finish.config(text='')
    label_name.config(text="Имя")
    label_last_name.config(text="Фамилия")
    label_phone_number.config(text="Номер телефона")
    label_description.config(text="Описание")
    entry_name = Entry(win,width = 30)
    entry_name.grid(row=1, column=2)
    entry_last_name = Entry(win,width = 30)
    entry_last_name.grid(row=2, column=2)
    entry_phone_number = Entry(win,width = 30)
    entry_phone_number.grid(row=3, column=2)
    entry_description = Entry(win,width = 30)
    entry_description.grid(row=4, column=2, pady = 15)
    btn_enter = Button(win, text=f"Enter",
                font=('Courier New', 12, 'bold'),
                fg="#ff9933",
                bg="#ffe6cc",
                height=1,
                width=10,
                command=lambda: [entry_name.grid_forget(), 
                                entry_last_name.grid_forget(),
                                entry_phone_number.grid_forget(),
                                entry_description.grid_forget(),
                                make_new_contact(), 
                                change_label_add(),
                                clear_labels(),
                                db.add_contact(contact), 
                                btn_enter.grid_forget()])
    btn_enter.grid(row=5, column=2, pady = 10)

def delete_contact():
    global entry_name
    label_instruction.config(text='Введите id контакта:\nЧтобы его узнать воспользуйтесь\n"Найти контакт"')
    entry_name.grid_forget(), 
    entry_last_name.grid_forget(),
    entry_phone_number.grid_forget(),
    entry_description.grid_forget()
    clear_labels()
    label_finish.config(text='')
    label_name.config(text="ID")
    entry_name = Entry(win,width = 30)
    entry_name.grid(row=1, column=2)
    btn_enter = Button(win, text=f"Enter",
                       font=('Courier New', 12, 'bold'),
                       fg="#ff9933",
                       bg="#ffe6cc",
                       height=1,
                       width=10,
                       command=lambda: [entry_name.grid_forget(),
                                        take_id(),
                                        db.delete_contact(id),
                                        change_label_del(),
                                        clear_labels(),
                                        btn_enter.grid_forget()])
    btn_enter.grid(row=5, column=2, pady = 10)

def find_contact():
    global entry_name
    label_instruction.config(text='Введите имя:')
    entry_name.grid_forget(), 
    entry_last_name.grid_forget(),
    entry_phone_number.grid_forget(),
    entry_description.grid_forget()
    clear_labels()
    label_finish.config(text='')
    label_name.config(text="Имя")
    entry_name = Entry(win,width = 30)
    entry_name.grid(row=1, column=2)
    btn_enter = Button(win, text=f"Enter",
                   font=('Courier New', 12, 'bold'),
                   fg="#ff9933",
                   bg="#ffe6cc",
                   height=1,
                   width=10,
                   command=lambda: [entry_name.grid_forget(),
                                    clear_labels(),
                                    change_label_find(db.find_contact(take_name())),
                                    btn_enter.grid_forget()])
    btn_enter.grid(row=5, column=2, pady = 10)
def take_name():
    name = entry_name.get()
    return name
def take_id():
    global id
    id = entry_name.get()
    return id

def change_label_add():
    label_finish.config(text='Контакт добавлен')
def change_label_del():
    label_finish.config(text='Контакт удален')
def change_label_find(list):
    label_finish.config(text=f'Контакты{list}')

def clear_labels():
    label_name.config(text="")
    label_last_name.config(text="")
    label_phone_number.config(text="")
    label_description.config(text="")

def make_new_contact():
    global contact
    name = entry_name.get()
    last_name = entry_last_name.get()
    phone_number = entry_phone_number.get()
    phone_number = int(phone_number)
    description = entry_description.get()
    contact = (name, last_name, phone_number, description)
    return contact    



win = Tk()
win.title("PHONEBOOK") 
win.geometry("600x400+500+200")
win.resizable(False, False)
win.config(bg="#3399ff")

btn1 = Button(  text=f"Добавить контакт",
                 font=('Courier New', 12, 'bold'),
                fg="#ff9933",
                bg="#ffe6cc",
                height=1,
                width=16,
                command=lambda: add_contact()) 
btn1.grid(row=1, column=0, pady = 10)
btn2 = Button(win, text=f"Найти контакт",
                 font=('Courier New', 12, 'bold'),
                fg="#ff9933",
                bg="#ffe6cc",
                height=1,
                width=16,
                command=lambda: find_contact())
btn2.grid(row=2, column=0, pady = 10)
btn3 = Button(win, text=f"Удалить контакт",
                 font=('Courier New', 12, 'bold'),
                fg="#ff9933",
                bg="#ffe6cc",
                height=1,
                width=16,
                command=lambda: delete_contact()) 
btn3.grid(row=3, column=0, pady = 10)

label = Label(text='Phone book\nВыбери функцию:', font=('Arial', 14), width=20, bg="#3399ff")
label.grid(row=0, column=0)
label_name = Label(text="", width=16, bg="#3399ff")
label_name.grid(row=1, column=1)
label_last_name = Label(text="", width=16, bg="#3399ff")
label_last_name.grid(row=2, column=1)
label_phone_number = Label(text="", width=16, bg="#3399ff")
label_phone_number.grid(row=3, column=1)
label_description = Label(text="", width=16, bg="#3399ff")
label_description.grid(row=4, column=1)
label_instruction = Label(text="", width=16, bg="#3399ff")
label_instruction.grid(row=0, column=2, sticky='we')
label_finish = Label(text='',width = 16, font= 20, bg="#3399ff")
label_finish.grid(row=6, column=0, columnspan=4, sticky='we')

entry_name = Entry(win,width = 30)
entry_name.grid(row=1, column=2)
entry_last_name = Entry(win,width = 30)
entry_last_name.grid(row=2, column=2)
entry_phone_number = Entry(win,width = 30)
entry_phone_number.grid(row=3, column=2)
entry_description = Entry(win,width = 30)
entry_description.grid(row=4, column=2)
entry_name.grid_forget() 
entry_last_name.grid_forget()
entry_phone_number.grid_forget()
entry_description.grid_forget()
win.mainloop()