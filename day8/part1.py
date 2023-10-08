def part1():
    lines = open('input.txt','r').readlines()
    grid=[]
    vis=[]
    for line in lines:
        vis2=[]
        row = []
        for d in line:
            if(d=='\n'): continue
            vis2.append(0)
            row.append(int(d))
        grid.append(row)
        vis.append(vis2)
    
    for row in range(1,len(grid)-1):
        tallest=0
        for col in range(1,len(grid[0])-1):
            if(grid[row][col]>grid[row][tallest]):
                vis[row][col]=1
                tallest=col
        tallest=len(grid[0])-1
        for col in range(1,len(grid[0])-1):
            col=len(grid[0])-col-1
            if(grid[row][col]>grid[row][tallest]):
                vis[row][col]=1
                tallest=col
    for col in range(1,len(grid[0])-1):
        tallest=0
        for row in range(1,len(grid)-1):
            if(grid[row][col]>grid[tallest][col]):
                tallest=row
                vis[row][col]=1
        tallest=len(grid)-1
        for row in range(1,len(grid)-1):
            row = len(grid)-row-1
            if(grid[row][col]>grid[tallest][col]):
                tallest=row
                vis[row][col]=1
    count=2*(len(grid)+len(grid[0]))-4
    for row in range(1,len(grid)-1):
        for col in range(1,len(grid[0])-1):
            count+=vis[row][col]
    print(count)
    
part1()
input()