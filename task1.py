# Перше завдання
# Створіть функцію get_days_from_today(date), яка розраховує
# кількість днів між заданою датою і поточною датою.

from datetime import datetime, timedelta


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        days = (date - today).days + 1
        return days
    except ValueError:
        return "Не коректний формат дати!"


print(get_days_from_today('2024-06-18'))
