def read_txt(filename):
    phone_book = []

    try:
        with open(filename, 'r', encoding='utf-8') as phb:
            for line in phb:
                record = dict(zip(['Фамилия', 'Имя', 'Телефон', 'Описание'], line.strip().split(',')))
                phone_book.append(record)
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создайте файл и добавьте данные.")
    
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            line = ','.join(record.values())
            phout.write(f'{line}\n')

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменить номер телефона абонента\n"
          "4. Удалить абонента по фамилии\n"
          "5. Найти абонента по номеру телефона\n"
          "6. Добавить абонента в справочник\n"
          "7. Скопировать данные из файла\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

# Placeholder functions
def print_result(phone_book):
    print("Print result placeholder")

def find_by_lastname(phone_book, last_name):
    print("Find by lastname placeholder")

def change_number(phone_book, last_name, new_number):
    print("Change number placeholder")

def delete_by_lastname(phone_book, last_name):
    print("Delete by lastname placeholder")

def find_by_number(phone_book, number):
    print("Find by number placeholder")

def add_user(phone_book, user_data):
    print("Add user placeholder")

def copy_data_from_file():
    print("Copy data from file placeholder")

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')

    while choice != 8:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('lastname ')
            find_by_lastname(phone_book, last_name)
        elif choice == 3:
            last_name = input('lastname ')
            new_number = input('new  number ')
            change_number(phone_book, last_name, new_number)
        elif choice == 4:
            lastname = input('lastname ')
            delete_by_lastname(phone_book, lastname)
        elif choice == 5:
            number = input('number ')
            find_by_number(phone_book, number)
        elif choice == 6:
            user_data = input('new data ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 7:  
            copy_data_from_file()
            print("Data copied successfully!")

        choice = show_menu()

if __name__ == "__main__":
    work_with_phonebook()
