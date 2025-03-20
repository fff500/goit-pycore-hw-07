from collections import UserDict
from datetime import date, datetime

from utils import find_element

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

    def __repr__(self):
        return f"Phone({self.value})"

class Birthday(Field):
    def __init__(self, value):
        try:
            day, month, year = list(map(int, value.split('.')))
            date_obj = date(year, month, day)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(date_obj)

class Record:
    def __init__(self, name, phones=[], birthday = None):
        self.name = Name(name)
        self.phones = phones
        self.birthday = birthday

    def add_birthday(self, birthdate):
        self.birthday = Birthday(birthdate)

    def add_phone(self, phone):
        if not self.find_phone(phone):
            self.phones.append(Phone(phone))
        else:
            raise KeyError("Phone already exists.")

    def delete_phone(self, phone):
        self.phones = filter(lambda x: x.value != phone, self.phones)

    def edit_phone(self, phone, new_phone):
        self.phones = list(map(lambda x: Phone(new_phone) if x.value == phone else x, self.phones))

    def find_phone(self, phone):
        return find_element(self.phones, lambda x: x.value == phone)
    
    def __repr__(self):
        return f"Record({self.name.value}, {self.phones}, {self.birthday})"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name] if name in self.data.keys() else None
    
    def delete(self, name):
        self.data.pop(name)

    def get_upcoming_birthdays(self):
        cur_year = datetime.now().year
        today = date.today().timetuple().tm_yday
        greetings = []

        for user in self.data:
            b_day_date = user['birthday']
            b_day_number = b_day_date.timetuple().tm_yday
            b_day_month = b_day_date.month
            b_day_day = b_day_date.day
            b_day_week_day = datetime.strptime( \
                    str(cur_year) + "." + str(b_day_month) + "." + str(b_day_day), "%Y.%m.%d" \
                ).weekday()

            if today <= b_day_number <= today + 7:
                if b_day_week_day == 5:
                    b_day_number += 2
                if b_day_week_day == 6:
                    b_day_number += 1
            
            congrats_date = datetime.strptime(str(cur_year) + "." + str(b_day_number), "%Y.%j").strftime("%Y.%m.%d")
            greetings.append({"name": user['name'], "congratulation_date": congrats_date})

        print(greetings)
        return greetings
