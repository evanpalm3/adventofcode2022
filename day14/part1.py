def printGrid(g,xmin,ymin):
    for y in range(len(g)):
        if(y<ymin):
            continue
        s=""
        for x in range(len(g[0])):
            if(x>=xmin):
                v=g[y][x]
                if(v==1):
                    s+='#'
                elif(v==0):
                    s+='.'
                else:
                    s+='o'
        print(s)

def part1():
    lines = open('input.txt','r').readlines()
    xmax=0
    xmin=100000
    ymax=0
    ymin=100000
    rocklines=[]
    for line in lines:
        parts=line.split(' -> ')
        last=0
        for part in parts:
            coords=part.split(',')
            x=int(coords[0])
            y=int(coords[1])
            point=[x,y]
            if(x>xmax):
                xmax=x
            elif(x<xmin):
                xmin=x
            if(y>ymax):
                ymax=y
            elif(y<ymin):
                ymin=y
            if(last!=0):
                rocklines.append([last,point])
            last=point
    g=[]
    for i in range(ymax+2):
        p=[]
        for k in range(xmax+2):
            p.append(0)
        g.append(p)
    for rocks in rocklines:
        r1=rocks[0]
        r2=rocks[1]
        if(r1[0]==r2[0]):
            inc=1
            if(r2[1]<r1[1]):
                inc=-1
            for y in range(r1[1],r2[1],inc):
                g[y][r1[0]]=1
        else:
            inc=1
            if(r2[0]<r1[0]):
                inc=-1
            for x in range(r1[0],r2[0],inc):
                g[r1[1]][x]=1
        g[r2[1]][r2[0]]=1
    running=True
    x=500
    y=0
    count=0
    while(running):
        if(g[y+1][x]==0):
            y+=1
        elif(g[y+1][x-1]==0):
            y+=1
            x-=1
        elif(g[y+1][x+1]==0):
            y+=1
            x+=1
        else:
            g[y][x]=2
            count+=1
            x=500
            y=0
        if(y==ymax):
            running=False
    print(count)
    #printGrid(g,xmin,ymin)
    
part1()
input()
