import sys

# ans[date,month,year,working days]

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



inp=sys.argv
print(fun(inp))