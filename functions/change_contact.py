from classes.address_book import AddressBook

def input_error(func):
    def inner(*args, **kwargs):
        try:
            if len(args[0]) != 3:
                raise ValueError
            if not args[1].find(args[0][0]):
                raise KeyError("Such contact doesn't exist.")
            return func(*args, **kwargs)
        except KeyError:
            return "Such contact or phone doesn't exist."
        except ValueError:
            return "Give me a name, phone to change and new phone, please."

    return inner

@input_error
def change_contact(args, book: AddressBook):
    name, existing_phone, new_phone, *_ = args
    book.find(name).edit_phone(existing_phone, new_phone)
    return "Contact changed."