# import datetime 
# A = datetime.datetime(2005,6,15)
# D = datetime.datetime(2003,12,19)
# print(A.strftime("%x"))
# print(D.strftime("%x"))
from datetime import datetime as date
a = date.now()
print(a.replace(microsecond = 0))