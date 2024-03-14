import datetime as dt

date1=dt.date(2024,2,23)
date2=dt.date(2024,3,12)
date2=date2+dt.timedelta(days=1)
h_list=[dt.date(2024,1,1),dt.date(2024,1,15),dt.date(2024,1,26),dt.date(2024,3,25),dt.date(2024,5,1),dt.date(2024,6,17),dt.date(2024,8,15),dt.date(2024,9,7),dt.date(2024,10,2),dt.date(2024,10,12),dt.date(2024,10,31),dt.date(2024,11,1),dt.date(2023,9,19),dt.date(2023,10,2),dt.date(2023,10,24),dt.date(2023,12,25),]

working_days_for_project=[]

while date1!=date2:
    
    if date1.weekday()==6:
        date1=date1+dt.timedelta(days=1)
        continue
    elif date1 in h_list:
        date1=date1+dt.timedelta(days=1)
        continue
    else:
        working_days_for_project.append(date1)
        date1=date1+dt.timedelta(days=1)

print(len(working_days_for_project))
