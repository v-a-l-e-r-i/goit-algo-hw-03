# Друге завдання
# Щоб виграти головний приз лотереї, необхідний збіг кількох номерів
# на лотерейному квитку з числами, що випали випадковим чином і в певному
# діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість
# чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

from random import sample


def get_numbers_ticket(min_num, max_num, quantity):
    try:
        return sorted(sample(range(min_num, max_num), k=quantity))
    except ValueError:
        return []


lottery_numbers = get_numbers_ticket(10,14,6)
print("Ваші лотерейні числа:", lottery_numbers)