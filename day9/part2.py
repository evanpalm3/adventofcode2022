def distance(t,h):
    return max(abs(t[0]-h[0]),abs(t[1]-h[1]))

def printGrid(h, t, width, height):
    grid=[]
    for i in range(width):
        d=[]
        for k in range(height):
            d.append('.')
        grid.append(d)
    f=0
    for ti in t:
        f+=1
        grid[ti[0]][ti[1]]=str(f)
    grid[h[0]][h[1]]='H'
    for y in range(height):
        s=""
        for x in range(width):
            s+=grid[x][y]
        print(s)

def chain(h,t):
    if(distance(t,h)<2):
        return
    if(h[0]==t[0]):
        if(h[1]==t[1]):
            return
        if(h[1]>t[1]):
            t[1]+=1
            return
        t[1]-=1
        return
    if(h[1]==t[1]):
        if(h[0]>t[0]):
            t[0]+=1
            return
        t[0]-=1
        return
    if(h[0]>t[0]):
        t[0]+=1
    else:
        t[0]-=1
    if(h[1]>t[1]):
        t[1]+=1
    else:
        t[1]-=1
        

def move(h,t,d):
    hold=[h[0],h[1]]
    if(d=='U'):
        h[1]=h[1]+1
        if(distance(t,h)>1):
            t[0]=hold[0]
            t[1]=hold[1]
    if(d=='D'):
        h[1]=h[1]-1
        if(distance(t,h)>1):
            t[0]=hold[0]
            t[1]=hold[1]
    if(d=='R'):
        h[0]=h[0]+1
        if(distance(t,h)>1):
            t[0]=hold[0]
            t[1]=hold[1]
    if(d=='L'):
        h[0]=h[0]-1
        if(distance(t,h)>1):
            t[0]=hold[0]
            t[1]=hold[1]
                
def part2():
    lines = open('input.txt', 'r').readlines()
    x=0
    y=0
    xmin=0
    xmax=0
    ymin=0
    ymax=0
    for line in lines:
        words = line.split(' ')
        if(line[0]=='U'):
            y+=int(words[1])
            if(y>ymax):
                ymax=y
                continue
        if(line[0]=='D'):
            y-=int(words[1])
            if(y<ymin):
                ymin=y
        if(line[0]=='R'):
            x+=int(words[1])
            if(x>xmax):
                xmax=x
        if(line[0]=='L'):
            x-=int(words[1])
            if(x<xmin):
                xmin=x
    width=xmax+(-1)*xmin+1
    height=ymax+(-1)*ymin+1
    grid=[]
    for i in range(width):
        d=[]
        for k in range(height):
            d.append(0)
        grid.append(d)
    h=[-1*xmin,-1*ymin]
    s=[]
    t=[]
    for i in range(9):
        k=[h[0],h[1]]
        t.append(k)
        if(i==8):
            s=k
    grid[s[0]][s[1]]=1
    for line in lines:
        words = line.split(' ')
        d = line[0]
        n = int(words[1])
        for i in range(n):
            move(h,t[0],d)
            for k in range(len(t)-1):
                chain(t[k],t[k+1])
            grid[s[0]][s[1]]=1
            #printGrid(h,t,int(width/3),int(height/8))
            #input()
    sum=0
    for x in range(width):
        for y in range(height):
            sum+=grid[x][y]
    print(sum)

#part1()
part2()
input()

