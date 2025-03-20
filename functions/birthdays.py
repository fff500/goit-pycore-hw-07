from classes.address_book import AddressBook

def birthdays(book: AddressBook):
    return book.get_upcoming_birthdays()