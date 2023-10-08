def strA(s,i,c):
    t=""
    for k in range(len(s)):
        if(k==i):
            t+=c
        else:
            t+=s[k]
    return t

def strR(s,c):
    t=""
    for k in range(len(s)):
        if(s[k]!=c):
            t+=s[k]
    return t

def max(a,b):
    if(a>b):
        return a
    return b

def build(s):
    data=[]
    if(len(s)==0):
        return data
    count=0
    for k in range(len(s)):
        if(s[k]==','):
            if(count==0):
                s=strA(s,k,'*')
        elif(s[k]=='['):
            count+=1
        elif(s[k]==']'):
            count-=1
    stuf=s.split('*')
    for k in stuf:
        if(k[0]=='['):
            data.append(build(k[1:len(k)-1]))
        else:
            data.append(int(k))
    return data

def compare(l,r):
    if(type(l) is int and type(r) is int):
        if(l<r):
            return 'c'
        elif(l==r):
            return 'u'
        else:
            return 'w'
    elif(type(l) is list and type(r) is list):
        for i in range(max(len(l),len(r))):
            if(i==len(l)):
                return 'c'
            elif(i==len(r)):
                return 'w'
            res=compare(l[i],r[i])
            if(res!='u'):
                return res
        return 'u'
    else:
        if(type(l) is int):
            return compare([l],r)
        return compare(l,[r])

def part1():
    lines = open('input.txt', 'r').readlines()
    sum=0
    for i in range(int((1+len(lines))/3)):
        lstr=strR(lines[3*i],'\n')
        left=build(lstr[1:len(lstr)-1])
        rstr=strR(lines[3*i+1],'\n')
        right=build(rstr[1:len(rstr)-1])
        if(compare(left,right)=='c'):
            sum+=i+1
    print(sum)

part1()
input()
