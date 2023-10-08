def part2():
    lines = open('input.txt', 'r').readlines()
    count=0
    for line in lines:
        ranges = line.split(',')
        r1=ranges[0].split('-')
        r2=ranges[1].split('-')
        if(int(r1[0])>int(r2[0])):
            r3=r2
            r2=r1
            r1=r3
        if(int(r1[1])>=int(r2[0])):
            count+=1
    print(count)

part2()
input()
