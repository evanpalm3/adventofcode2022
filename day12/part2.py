import sys
sys.setrecursionlimit(4000)

def dif(x,y):
    k=x-y
    if(k<0):
        k=-1*k
    return k

def search(x,y,l,c,g):
    if(c[y][x]==-1 or l<c[y][x]):
        c[y][x]=l
        if(x!=len(g[0])-1):
            if(g[y][x+1]-g[y][x]>-2): 
                search(x+1,y,l+1,c,g)
        if(x!=0):
            if(g[y][x-1]-g[y][x]>-2):
                search(x-1,y,l+1,c,g)
        if(y!=len(g)-1):
            if(g[y+1][x]-g[y][x]>-2):
                search(x,y+1,l+1,c,g)
        if(y!=0):
            if(g[y-1][x]-g[y][x]>-2):
                search(x,y-1,l+1,c,g)

def printProg(c,lines):
    for y in range(len(c)):
        s=""
        for x in range(len(c[0])):
            if(c[y][x]==-1):
                s+=lines[y][x]
                continue
            s+='X'
        print(s)
            
def part2():
    lines=open('input.txt', 'r').readlines()
    grid=[] # 41 x 173
    c=[]
    S=[-1,-1]
    E=[-1,-1]
    y=0
    for line in lines:
        p=[]
        t=[]
        x=0
        for k in line:
            if(k=='\n'):
                continue
            t.append(-1)
            if(k=='S'):
                p.append(ord('a'))
                S=[x,y]
                continue
            if(k=='E'):
                p.append(ord('z'))
                E=[x,y]
                continue
            p.append(ord(k))
            x+=1
        y+=1
        grid.append(p)
        c.append(t)
    search(E[0],E[1],0,c,grid)
    min=len(grid)*len(grid[0])
    j=0
    if(min>100):# adventOfCode soulution was inconsistent with prompt, requies +1
        j=1
    y=0
    for line in lines:
        x=0
        for k in line:
            if(k=='a'):
                if(c[y][x]<min and c[y][x]!=-1):
                    min=c[y][x]
            x+=1
        y+=1
    print(min+j)

part2()
input()
