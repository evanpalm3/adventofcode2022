def part1():
    lines = open("input.txt","r").readlines()
    count=0
    greatest=0
    for line in lines:
        if(line[0]=='\n'):
            if(count>greatest):
                greatest=count
            count=0
        else:
            count+=int(line)
    print(greatest)
    
part1()
input()