def part2():
    lines = open("input.txt","r").readlines()
    count=0
    cals=[]
    for line in lines:
        if(line[0]=='\n'):
            cals.append(count)
            count=0
        else:
            count+=int(line)
    cals.sort()
    sum=0
    for i in range(3):
        sum+=cals[len(cals)-1-i]
    print(sum)

part2()
input()
