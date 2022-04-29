class Note(object):
    def __init__(self):
        self.listNote = []

    def __contains__(self, info):
        return info in self.listNote

    def __len__(self):
        return len(self.listNote)

    class Info(object):
        def __init__(self, surname, name, telephone_number, birthday=None):
            if birthday is None:
                birthday = []
            self.surname = surname
            self.name = name
            self.telephone_number = telephone_number
            self.birthday = birthday

        #def __contains__(self, attr):
        #    return attr in {self.surname, self.name, self.telephone_number, self.birthday}

        def show_info(self):
            print(f"Фамилия: {self.surname}")
            print(f"Имя: {self.name}")
            print(f"Дата рождения: ")
            for i in range(3):
                print(self.birthday[i])

    def add(self, surname, name, telephone_number, birthday=None):
        if birthday is None:
            birthday = []
        self.listNote.append(self.Info(surname, name, telephone_number, birthday))

    def search(self, telephone_number):
        temp = 1
        for info in self.listNote:
            if telephone_number in info.telephone_number:
                info.show_info()
                temp = 0
        if temp == 1:
            print("Человек с таким номером не найден!")

    def sort(self):
        list.sort(self.listNote, key=lambda info: info.birthday)

    def show(self):
        for info in self.listNote:
            print(f"Фамилия: {info.surname}")
            print(f"Имя: {info.name}")
            print(f"Номер телефона: {info.telephone_number}")
            print(f"Дата рождения: {info.birthday}\n")


def main():
    note_size = 8
    note = Note()
    for number_people in range(note_size):
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        telephone_number = input("Введите номер телефона: ")
        print("Введите дату рождения: ")
        birthday = []
        for date in range(3):
            date1 = int(input())
            birthday.append(date1)
        note.add(surname, name, telephone_number, birthday)

    note.sort()
    note.show()

    telephone_number = input("Введите номер телефона искомого человека: ")
    note.search(telephone_number)


if __name__ == "__main__":
    main()
