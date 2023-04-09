# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# Добавление записи в справочник
def Phone_number():
    surname = input("Фамилия: ")
    name = input("Имя: ")
    lastname = input("Отчество: ")
    tel = input("Телефон: ")
    with open("phone_number.txt", "a", encoding="utf-8") as data:
        data.write(f"Фамилия: {surname} ")
        data.write(f"Имя: {name} ")
        data.write(f"Отчество: {lastname} ")
        data.write(f"Телефон: {tel} \n")
        data.close()

# Печать справочника
def ShowData():
    with open("phone_number.txt", "r", encoding="utf-8") as data:
        for line in data:
            print(line)

# Удаление данных

def DeleteData():
    lookfor = input("Кого хотите удалить? ")
    with open("phone_number.txt", "r", encoding="utf-8") as data:
        person = data.readlines()
        with open("phone_number.txt", "w", encoding="utf-8") as data_1:
            for pers in person:
                if lookfor not in pers:
                    data_1.write(pers)
                else:
                    print(pers)
                    question = input("Вы хотите удалить эту строку? Yes - да, No - нет ")
                    if question == "No":
                        data_1.write(pers)

# Изменение данных                              
def ChangeData():
    lookfor = input("Какую запись хотите скорректиовать? ")
    with open("phone_number.txt", "r", encoding="utf-8") as data:
        person = data.readlines()
        with open("phone_number.txt", "w", encoding="utf-8") as data_1:
            for pers in person:
                if lookfor not in pers:
                    data_1.write(pers)
                else:
                    surname = input("Новая фамилия: ")
                    name = input("Новое имя: ")
                    lastname = input("Новое отчество: ")
                    tel = input("Новый телефон: ")
                    data_1.write(f"{surname}\t{name}\t{lastname}\t{tel}")


# Запрос действия у пользователя
print(""" Что вы хотите сделать?
1 - Добавление записи в справочник
2 - Вывод справочника на экран
3 - Удаление данных
4 - Изменение данных """)

user_input = int(input()) 
if user_input == 1:
    Phone_number()
elif user_input == 2:
    ShowData()
elif user_input == 3:    
    DeleteData()
elif user_input == 4:
    ChangeData()
else:
    print("Вы ввели некорректную команду")    

