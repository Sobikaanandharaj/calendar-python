import calendar
from datetime import date
from dateutil.relativedelta import relativedelta

def fullcal(y):
    print(calendar.calendar(y))

def dismon(y, m):
    print(calendar.month(y, m))

def holiday(month, day):
    holi = {
        (1,1): "New Year",
        (1, 14): "Pongal",
        (8, 15): "Independence Day",
        (12, 25): "Christmas"
    }
    if (month, day) in holi:
        print("Holiday : ", holi[(month, day)])
    else:
        print("No holiday noted on this date")

def birthday(year, month, day):
    bir = {
        (2006, 11, 13): "San Birthday",
        (2007, 5, 29): "Resu Birthday",
        (1997, 9, 1): "Jeon Birthday"
    }
    if (year, month, day) in bir:
        print("Birthday: ", bir[(year, month, day)])
    else:
        print("No birthday noted on this date")

def age(dob):
    today = date.today()
    diff = relativedelta(today, dob)
    print(f"Age: {diff.years} years, {diff.months} months, and {diff.days} days")

print(" ---------------- Fizzy Calendar --------------")
print()
print("1. Calendar")
print("2. Specific Month")
print("3. Holiday")
print("4. Birthday")
print("5. Age in years, months and days")
print()
a = int(input("Please Enter Your Choice: "))

if a == 1:
    y = int(input("Enter Year : "))
    fullcal(y)
elif a == 2:
    y = int(input("Enter Year : "))
    m = int(input("Enter Month : "))
    dismon(y, m)
elif a == 3:
    month = int(input("Enter a Month : "))
    day = int(input("Enter a Date : "))
    holiday(month, day)
elif a == 4:
    year = int(input("Enter a Year : "))
    month = int(input("Enter a Month : "))
    day = int(input("Enter a Date : "))
    birthday(year, month, day)
elif a == 5:
    d = input("Enter your DOB (YYYY-MM-DD) : ")
    dob = date.fromisoformat(d)
    age(dob)
