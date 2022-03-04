from datetime import datetime  as date,timedelta
today = date.now()
yesterday = date.now() - timedelta(days = 1)
tommorow = date.now() + timedelta(days = 1)
print(f'Yesterday {yesterday.strftime("%x")}')
print(f'Today {today.strftime("%x")}')
print(f'Tommorow {tommorow.strftime("%x")}')
