from classes.birthday import Birthday
from classes.name import Name
from classes.phone import Phone
from utils.utils import find_element

class Record:
    def __init__(self, name, phones=[], birthday = None):
        self.name = Name(name)
        self.phones = phones
        self.birthday = birthday

    def add_birthday(self, birthdate):
        self.birthday = Birthday(birthdate)

    def get_name(self):
        return self.name.value

    def get_birthday(self):
        return self.birthday.value if self.birthday else None

    def add_phone(self, phone):
        if not self.find_phone(phone):
            self.phones.append(Phone(phone))
        else:
            raise KeyError("Phone already exists.")

    def delete_phone(self, phone):
        self.phones = filter(lambda x: x.value != phone, self.phones)

    def edit_phone(self, phone, new_phone):
        existing_phone = find_element(self.phones, lambda x: x.value == phone)
        if not existing_phone:
            raise KeyError
        self.phones = list(map(lambda x: Phone(new_phone) if x.value == phone else x, self.phones))

    def find_phone(self, phone):
        return find_element(self.phones, lambda x: x.value == phone)
    
    def __repr__(self):
        return f"Record({self.name.value}, {self.phones}, {self.birthday})"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"