from classes.address_book import AddressBook

def input_error(func):
    def inner(*args, **kwargs):
        try:
            if len(args[0]) != 1:
                raise ValueError
            return func(*args, **kwargs)
        except ValueError:
            return "Give me a name, please."

    return inner

@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)

    if not record:
        return "Such contact doesn't exist."

    birthday = book.find(name).birthday

    if not birthday:
        return "This contact's birthday isn't indicated."

    return birthday