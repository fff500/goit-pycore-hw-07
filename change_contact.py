def input_error(func):
    def inner(*args, **kwargs):
        try:
            if len(args[0]) != 2:
                raise ValueError
            if not args[0][0] in args[1]:
                raise KeyError
            return func(*args, **kwargs)
        except KeyError:
            return "Such a contact doesn't exist."
        except ValueError:
            return "Give me name and phone, please."

    return inner

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."