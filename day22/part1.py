def move(rows,cols,x,y,d):
    if(d==0):
        if(x+1>rows[y][1]):
            return rows[y][0],y
        return x+1,y
    elif(d==2):
        if(x-1<rows[y][0]):
            return rows[y][1],y
        return x-1,y
    elif(d==1):
        if(y+1>cols[x][1]):
            return x,cols[x][0]
        return x,y+1
    elif(d==3):
        if(y-1<cols[x][0]):
            return x,cols[x][1]
        return x,y-1

def part1():
    lines = open('input.txt', 'r').readlines()
    grid=[]
    code=0
    maxx=0
    for line in lines:
        maxx=max(maxx,len(line))
        if(line=='\n'):
            code=-1
            continue
        if(code==-1):
            code=line[:len(line)-1]
            break
        grid.append(line[:len(line)-1])
    rows=[]
    cols=[]
    for row in grid:
        l=-1
        r=len(row)-1
        for i in range(len(row)):
            if(l==-1):
                if(row[i]!=' '):
                    l=i
                    continue
            else:
                if(row[i]==' '):
                    r=i-1
                    break
        rows.append([l,r])
    for col in range(maxx-1):
        t=-1
        b=len(grid)-1
        for row in range(len(grid)):
            if(t==-1):
                if(col<len(grid[row]) and grid[row][col]!=' '):
                    t=row
                continue
            else:
                if(col>=len(grid[row]) or grid[row][col]==' '):
                    b=row-1
                    break
        cols.append([t,b])
    indices=[]
    for k in range(len(code)):
        if(code[k]=='L' or code[k]=='R'):
            indices.append(k)
    dirs=[]
    for k in range(len(indices)+1):
        l=0
        r=len(code)
        if(k>0):
            l=indices[k-1]+1
            dirs.append(code[indices[k-1]])
        if(k<len(indices)):
            r=indices[k]
        dirs.append(int(code[l:r]))
    x=0
    y=0
    facing=0
    for i in range(len(grid[0])):
        if(grid[0][i]!=' '):
            x=i
            break
    for op in dirs:
        if(type(op) is int):
            for i in range(op):
                nx,ny=move(rows,cols,x,y,facing)
                if(grid[ny][nx]=='.'):
                    x=nx
                    y=ny
        else:
            if(op=='R'):
                facing=(facing+1)%4
            elif(op=='L'):
                facing-=1
                if(facing<0):
                    facing+=4
    print(1000*(y+1)+4*(x+1)+facing)
part1()
input()
