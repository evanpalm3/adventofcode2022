def calcScore(row, col, grid):
    down=0
    for y in range(row+1, len(grid)):
        down+=1
        if(grid[row][col]<=grid[y][col]):
            break
    up=0
    for y in range(0,row):
        up+=1
        if(grid[row][col]<=grid[row-1-y][col]):
            break
    right=0
    for x in range(col+1, len(grid[0])):
        right+=1
        if(grid[row][col]<=grid[row][x]):
            break
    left=0
    for x in range(0,col):
        left+=1
        if(grid[row][col]<=grid[row][col-x-1]):
            break
    return left*right*up*down

def part2():
    lines = open('input.txt','r').readlines()
    grid=[]
    for line in lines:
        row = []
        for d in line:
            if(d=='\n'): continue
            row.append(int(d))
        grid.append(row)
    highest=0
    for row in range(1,len(grid)-1):
        for col in range(1,len(grid[0])-1):
            d=calcScore(row,col,grid)
            if(d>highest): highest=d
    print(highest)

part2()
input()
