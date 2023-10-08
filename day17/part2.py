def printGrid(grid):
    for y in range(len(grid)):
        s=""
        for x in range(len(grid[0])):
            k=grid[len(grid)-1-y][x]
            if(k==1):
                s+='#'
            else:
                s+='.'
        print(s)

def max(a,b):
    if(a>b):
        return a
    return b

def intersect(x,y,shape,grid):
    for cy in range(len(shape)):
        for cx in range(len(shape[0])):
            if(shape[cy][cx]==1 and grid[y+cy][x+cx]==1):
                return True

def part2():
    dirs = open('input.txt', 'r').readlines()[0]
    modi=0
    if(dirs[len(dirs)-1]=='\n'):
        modi=-1
    shapes=[]
    shapes.append([[1,1,1,1]])
    shapes.append([[0,1,0],[1,1,1],[0,1,0]])
    shapes.append([[1,1,1],[0,0,1],[0,0,1]])
    shapes.append([[1],[1],[1],[1]])
    shapes.append([[1,1],[1,1]])
    grid=[]
    for i in range(7):
        grid.append([0,0,0,0,0,0,0])
    shapeI=0
    windI=0
    lastH=0
    patterns={}
    rock=0
    addative=0
    totalRocks=1000000000000
    while(rock<=totalRocks):
        rock+=1
        running=True
        y=lastH+3
        x=2
        shape=shapes[shapeI]
        f=len(grid)
        for k in range(f,lastH+7):
            grid.append([0,0,0,0,0,0,0])
        depth=40
        base=1
        for k in range(max(lastH-depth,0),lastH):
            for j in range(7):
                base=2*base+grid[k][j]
        key=(shapeI,windI,base)
        if(key in patterns):
            patternR=rock-patterns[key][1]
            patternH=lastH-patterns[key][0]
            jumps=int((totalRocks-rock)/patternR)
            addative+=jumps*patternH
            totalRocks-=patternR*jumps
        else:
            patterns[key]=[lastH,rock]
        while(running):
            wind=0
            if(dirs[windI]=='<'):
                wind=-1
                if(x+wind<0):
                    wind=0
            else:
                wind=1
                if(x+wind+len(shape[0])>7):
                    wind=0
            if(not intersect(x+wind,y,shape,grid)):
                x+=wind
            windI=(windI+1)%(len(dirs)+modi)
            stop=False
            if(y==0):
                stop=True
            elif(intersect(x,y-1,shape,grid)):
                stop=True
            else:
                y-=1
            if(stop):
                for cy in range(len(shape)):
                    for cx in range(len(shape[0])):
                        if(shape[cy][cx]==1):
                            grid[cy+y][cx+x]=1
                running=False
                g=y+len(shape)
                if(g>lastH):
                    lastH=g
        shapeI=(shapeI+1)%len(shapes)
    print(lastH+addative-1)

part2()
input()
