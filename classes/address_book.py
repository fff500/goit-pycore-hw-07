from collections import UserDict
from datetime import date, datetime

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

        for user in self.data.values():
            b_day_date = user.get_birthday()
            if b_day_date:
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
                greetings.append({"name": user.get_name(), "congratulation_date": congrats_date})

        return greetings