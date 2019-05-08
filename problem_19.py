import calendar
import datetime

start_date = datetime.date(1901, 1, 1) 
end_date = datetime.date(2000, 12, 1)


first_sundays = 0
for year in range(start_date.year, end_date.year+1):
    for month in range(start_date.month, end_date.month+1):
        date = datetime.date(year, month, 1)
        if date.weekday() == 6: # 6 is for Sunday
            first_sundays += 1
        
print(first_sundays)    

