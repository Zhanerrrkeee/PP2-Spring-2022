from datetime import datetime as date,timedelta
a = date.now().replace(microsecond = 0)
b = date(2003,12,19).replace(microsecond = 0)
c = a - b
print(int(c.total_seconds()))