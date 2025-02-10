day=int(input("Day: "))
month=int(input("Day: "))
year=int(input("Day: "))
day+=7
days_of_month=31
if month ==4 or month==6 or month==9 or month ==11:
    days_of_month=30
elif month==2:
    days_of_month=28
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            days_of_month = 29
if day>days_of_month:
    day-=days_of_month
    month+=1

    if month>12:
        month=1
        year+=1
print(f"Day:{day} Month: {month} Year:{year}")



