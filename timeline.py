

import datetime as dt
import sys

def fun(a):
    ans=[0,0,0,0]
    b=0
    for i in a:
        match i:
            case '-d':
                ans[0]=a[b+1]
            case '-m':
                ans[1]=a[b+1]
            case '-y':
                ans[2]=a[b+1]
            case '-w':
                ans[3]=a[b+1]
            case _:
                b+=1
                continue
        b+=1
    return ans

# ans[date,month,year,working days]

def time_take(year,month,date,time):
    date1=dt.date(year,month,date)
    date2=date1

    h_list=[dt.date(2024,1,1),dt.date(2024,1,15),dt.date(2024,1,26),dt.date(2024,3,25),dt.date(2024,5,1),dt.date(2024,6,17),dt.date(2024,8,15),dt.date(2024,9,7),dt.date(2024,10,2),dt.date(2024,10,12),dt.date(2024,10,31),dt.date(2024,11,1)]

    working_days_for_project=[]
    
    i=1
    while i!=(time+1):
        if date2.weekday()==6:
            date2=date2+dt.timedelta(days=1)
            continue
        elif date2 in h_list:
            date2=date2+dt.timedelta(days=1)
            continue
        else:
            working_days_for_project.append(date2)
            date2=date2+dt.timedelta(days=1)
            i+=1
    return working_days_for_project




def timeline_main():
    inp=fun(sys.argv)
    date=int(inp[0])
    month=int(inp[1])
    year=int(inp[2])

    working_days_for_project=time_take(year,month,date,time)
    time=int(inp[3])
        
    print(len(working_days_for_project))

    date_list={
        60:[0,29,34,36,37,42,43,44,44,48,49,50,59],
        75:[0,34,39,42,43,51,52,53,54,59,60,61,74,79],
        90:[0,39,44,47,48,57,58,59,59,64,66,67,89],
        105:[0,39,44,47,48,63,64,65,64,73,75,75,105],
        120:[0,39,46,49,50,69,70,70,70,81,84,85,119],
        135:[0,44,54,54,55,77,78,78,78,93,93,94,134],
        150:[0,49,59,59,60,85,86,86,86,103,103,104,149],
        180:[0,59,74,74,75,104,105,105,105,124,124,125,179]
            }

    if time==180:
        print("add extra 10 days")
    elif time==150 or time==135 or time==75:
        print("add extra 5 days")

    for i in date_list[time]:
        print(working_days_for_project[i].strftime("%d %b %Y"))


def workdone():
    inp=fun()