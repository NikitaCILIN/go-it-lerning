import datetime
user_day=input('Введить ваш день в форматі РРРР-ММ-ДД: ')
date=user_day
def get_days_from_today(date):
    try:
        input_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.datetime.today()
        difference = current_date - input_date
        return difference.days
    except ValueError:
        return "Неправильний формат вхідних даних. Потрібно використовувати формат 'РРРР-ММ-ДД' (наприклад, '2020-10-09')." 
    

print(get_days_from_today(date))  # Поверне різницю у днях 