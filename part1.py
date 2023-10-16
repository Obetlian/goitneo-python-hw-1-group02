from datetime import datetime, timedelta
from collections import defaultdict

# Функція для виведення іменинників на наступний тиждень
def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days < 7:
            day_of_week = birthday_this_year.weekday()

            # Якщо вихідний, ставимо на понеділок
            if day_of_week in [5, 6]:
                day_of_week = 0

            weekday_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][day_of_week]
            birthdays[weekday_name].append(name)

    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")


# Тестові дані
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 15)},
    {"name": "Jan Koum", "birthday": datetime(1976, 10, 18)},
    {"name": "Olena Ivanenko", "birthday": datetime(1994, 10, 19)},
    {"name": "Vitaliy Melnyk", "birthday": datetime(1989, 10, 21)},
    {"name": "Kateryna Shevchenko", "birthday": datetime(1992, 10, 16)},
    {"name": "Bohdan Petrenko", "birthday": datetime(1998, 10, 22)}
]

get_birthdays_per_week(users)
