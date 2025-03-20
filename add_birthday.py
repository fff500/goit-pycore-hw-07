from classes import AddressBook

def input_error(func):
    def inner(*args, **kwargs):
        try:
            if len(args[0]) != 2:
                raise ValueError
            if not args[1].find(args[0][0]):
                raise KeyError
            return func(*args, **kwargs)
        except KeyError:
            return "Such a contact doesn't exist."
        except ValueError:
            return "Give me name and birthday, please."

    return inner

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    record.add_birthday(birthday)
    return "Contact updated."