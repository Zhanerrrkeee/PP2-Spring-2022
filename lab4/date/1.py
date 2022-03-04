from datetime import datetime as date,timedelta
current_day = date.now()
day_5 = current_day - timedelta(days = 5)
print(f'Five days ago was {day_5.strftime("%x")}')
