from distutils.command.config import config
import imp
import mysql.connector
from zmq import curve_public
from config import host,user,password

mydb = mysql.connector.connect(host = 'localhost',user='root',password='Dimash2003')

cur = mydb.cursor()

cur.execute("show databases")

for i in cur:
    print(i)