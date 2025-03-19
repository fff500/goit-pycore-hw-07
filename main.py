from collections import UserDict
from datetime import date

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if len(value) < 2:
            raise TypeError("Name should have at least 2 characters")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() and not len(value) == 10:
            raise TypeError("Pnone number should have only 10 digits")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            day, month, year = list(map(int, value.split('.')))
            date_obj = date(year, month, day)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(date_obj)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        self.phones = filter(lambda x: x.value != phone, self.phones)

    def edit_phone(self, phone, new_phone):
        self.phones = list(map(lambda x: Phone(new_phone) if x.value == phone else x, self.phones))

    def find_phone(self, phone):
        return list(filter(lambda x: x.value == phone, self.phones))

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]
    
    def delete(self, name):
        self.data.pop(name)

bd12 = Birthday('01.01.2000')
print(bd12)