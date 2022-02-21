import math
from datetime import datetime
from dateutil import parser

print("HeLLo World!")

name = input("Enter your name: ")
print("HeLLo ", name)

name_lenth = len(name)
name_lenth_fact = math.factorial(name_lenth)
print("Your name has "+ str(name_lenth)+" letters. " +str(name_lenth)+"! = "+str(name_lenth_fact))

date = parser.parse(input("Please, enter your birth date in format (DD.MM.YYYY):"))
today = date.today()
age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
delta = today - date
print("Today is "+str(today.strftime('%d.%m.%y'))+", you are "+str(age)+" year ("+str(delta.days)+" days) old.")