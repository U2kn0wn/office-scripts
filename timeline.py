import datetime as dt
import sys
import calendar

time=0

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
                global time
                time=a[b+1]
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

    
    time=int(inp[3])
    working_days_for_project=time_take(year,month,date,time) 
    print(len(working_days_for_project))

    date_list={
        60:[0,29,34,36,37,42,43,44,44,48,49,50,59],
        75:[0,34,39,42,43,51,52,53,54,59,60,61,74],
        90:[0,39,44,47,48,57,58,59,59,64,66,67,89],
        105:[0,39,44,47,48,63,64,65,64,73,75,75,104],
        120:[0,39,46,49,50,69,70,70,70,81,84,85,119],
        135:[0,44,54,54,55,77,78,78,78,93,93,94,134],
        150:[0,49,59,59,60,85,86,86,86,103,103,104,149],
        180:[0,59,74,74,75,104,105,105,105,124,124,125,179]
            }
    
    ans=[]

    if time in date_list.keys():
        for i in date_list[time]:
            # print(working_days_for_project[i].strftime("%d/%b/%Y"))
            ans.append(working_days_for_project[i])
    else:
        for i in working_days_for_project:
            print(i.strftime("%d/%b/%Y"))
        exit()
    return ans



def month_cal(date1,date2):
    month=[24,25,25,26,26,24,27,26,24,24,25,26]
    lastdate=[31,29,31,30,31,30,31,31,30,31,30,31]
    ans=''
    start=date1
    startmont=int(start.month)
    end=date2
    endmont=int(end.month)
    ans+=str(dt.datetime.strptime(str(startmont),"%m").strftime("%b"))+": "+str(timecal(start,dt.datetime(2024,startmont,lastdate[startmont-1])))+"\n"
    startmont+=1
    while startmont != endmont:
        ans+=str(dt.datetime.strptime(str(startmont),"%m").strftime("%b"))+": "+str(month[startmont-1])+"\n"
        startmont+=1
    ans+=str(dt.datetime.strptime(str(startmont),"%m").strftime("%b"))+": "+str(timecal(dt.datetime(2024,endmont,1),end))+"\n"
    
    return ans



def text():
    timeline=timeline_main()
    timehere=time
    text=""
    text+="Pleases find the high level timelines.\n"
    text+="Total considered :"+str(timehere)+ " working days.\n"
    text+="Considered 6 Working Days.\n\n"
    months=month_cal(timeline[0],timeline[-1])
    text+=months
    text+="1. Kick start of production work: "+timeline[0].strftime("%d/%b/%Y")+".\n"
    text+="2. Floor covering, start of civil work, false ceiling work (If Any), electrical modification at site on or before: "+timeline[1].strftime("%d/%b/%Y")+".\n"
    text+="3. Expected date of completion of production work at factory: "+timeline[2].strftime("%d/%b/%Y")+".\n"
    text+="4. Dispatch to Site: "+timeline[3].strftime("%d/%b/%Y")+"\n"
    text+="5. Assembly of carcass at site starts from "+timeline[4].strftime("%d/%b/%Y")+" & all the photos will be shared as the work proceeds.\n"
    text+="6. Completion of Carcass assembly: "+timeline[5].strftime("%d/%b/%Y")+".\n"
    text+="7. Next 45% payment: "+timeline[6].strftime("%d/%b/%Y")+".\n"
    text+="8. Site Manual Work (If any) starts at: "+timeline[7].strftime("%d/%b/%Y")+".\n"
    text+="9. Doors measurement & door preparation & hardware procurement starts from "+timeline[8].strftime("%d/%b/%Y")+".\n"
    text+="10. Doors manufacturing completion at factory by "+timeline[9].strftime("%d/%b/%Y")+".\n"
    text+="11. Packing & Shifting of doors materials to site including hardware "+timeline[10].strftime("%d/%b/%Y")+".\n"
    text+="12. Assembly of shutters starts from "+timeline[11].strftime("%d/%b/%Y")+".\n"
    text+="13. Completion of entire wood work assembly including slab placement, painting (if part of quotation) & cleaning on or before "+timeline[12].strftime("%d/%b/%Y")+".\n"

    print(text)

def timecal(date1,date2):
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
        
    return len(working_days_for_project)+1



text()

date_list={
    60:[0,29,34,36,37,42,43,44,44,48,49,50,59],
    75:[0,34,39,42,43,51,52,53,54,59,60,61,74],
    90:[0,39,44,47,48,57,58,59,59,64,66,67,89],
    105:[0,39,44,47,48,63,64,65,64,73,75,75,104],
    120:[0,39,46,49,50,69,70,70,70,81,84,85,119],
    135:[0,44,54,54,55,77,78,78,78,93,93,94,134],
    150:[0,49,59,59,60,85,86,86,86,103,103,104,149],
    180:[0,59,74,74,75,104,105,105,105,124,124,125,179]
    }
    
