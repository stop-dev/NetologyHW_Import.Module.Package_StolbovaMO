from  application.salary import calculate_salary
from  application.db.people import get_employees
from datetime import datetime
from colorama import Fore, Back, Style

def what_day_is_it_today():
    date_now = datetime.now()
    print(Back.GREEN, end='')
    print(date_now.strftime("%a, %d %b %Y" + Style.RESET_ALL))

if __name__ == '__main__':
    what_day_is_it_today()
    calculate_salary()
    get_employees()

