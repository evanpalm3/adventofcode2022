def distance(t,h):
    return max(abs(t[0]-h[0]),abs(t[1]-h[1]))

def part1():
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
    t=[h[0],h[1]]
    grid[t[0]][t[1]]=1
    for line in lines:
        words = line.split(' ')
        hold=[h[0],h[1]]
        if(line[0]=='U'):
            for i in range(int(words[1])):
                h[1]=h[1]+1
                if(distance(t,h)>1):
                    t=hold
                    grid[t[0]][t[1]]=1
                hold=[h[0],h[1]]
        if(line[0]=='D'):
            for i in range(int(words[1])):
                h[1]=h[1]-1
                if(distance(t,h)>1):
                    t=hold
                    grid[t[0]][t[1]]=1
                hold=[h[0],h[1]]
        if(line[0]=='R'):
            for i in range(int(words[1])):
                h[0]=h[0]+1
                if(distance(t,h)>1):
                    t=hold
                    grid[t[0]][t[1]]=1
                hold=[h[0],h[1]]
        if(line[0]=='L'):
            for i in range(int(words[1])):
                h[0]=h[0]-1
                if(distance(t,h)>1):
                    t=hold
                    grid[t[0]][t[1]]=1
                hold=[h[0],h[1]]
    sum=0
    for x in range(width):
        for y in range(height):
            sum+=grid[x][y]
    print(sum)
    
part1()
input()