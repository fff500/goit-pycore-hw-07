from classes import AddressBook, Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone, please."

    return inner

@input_error
def add_contact(args, book: AddressBook):
    print(args)
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    message = "Contact added."
    book.add_record(record)
    return message