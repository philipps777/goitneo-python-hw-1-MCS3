
from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):

    birthday_dict = defaultdict(list)


    today = datetime.today().date()


    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()


        birthday_this_year = birthday.replace(year=today.year)


        delta_days = (birthday_this_year - today).days


        birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")


        if delta_days >= 0 and delta_days < 7:
            if birthday_weekday in ["Saturday", "Sunday"]:
                birthday_weekday = "Monday"


        birthday_dict[birthday_weekday].append(name)


    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")



users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jill Valentine", "birthday": datetime(1984, 3, 18)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jan Koum", "birthday": datetime(1974, 6, 19)},
]

get_birthdays_per_week(users)
