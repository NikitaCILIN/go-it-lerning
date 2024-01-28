import datetime
user_day=input('Введіть вашу дату в форматі РРРР-ММ-ДД: ')
date=user_day
def get_days_from_today(date):
    while True:
        try:
            input_date = datetime.datetime.strptime(date, '%Y-%m-%d')
            current_date = datetime.datetime.today()
            difference = current_date - input_date
            return difference.days
        except ValueError:
            print("Неправильний формат вхідних даних. \
                  Потрібно використовувати формат  'РРРР-ММ-ДД' (наприклад, '2020-10-09').")
            date = input("Будь ласка, введіть коректну дату у форматі 'РРРР-ММ-ДД': ")

print(get_days_from_today(date))  # Поверне різницю у днях 