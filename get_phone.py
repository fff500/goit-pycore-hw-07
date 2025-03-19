def input_error(func):
    def inner(*args, **kwargs):
        try:
            if len(args[0]) != 1:
                raise ValueError
            return func(*args, **kwargs)
        except KeyError:
            return "Such a contact doesn't exist."
        except ValueError:
            return "Give me a name, please."

    return inner

@input_error
def get_phone(args, contacts):
    return contacts[args[0]]