from classes.address_book import AddressBook
from classes.record import Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone, please."
        except KeyError:
            return "Phone already exists."

    return inner

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    message = "Contact updated."
    record = book.find(name)

    if not record:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    if phone:
        record.add_phone(phone)
    return message