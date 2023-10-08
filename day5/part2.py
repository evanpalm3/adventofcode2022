def part2():
    lines = open('input.txt', 'r').readlines()
    stacks=[]
    for i in range(int(len(lines[0])/4)):
        stacks.append([])
    count=0
    for line in lines:
        count+=1
        if(line[1]=='1'):
            break
        for i in range(int(len(lines[0])/4)):
            if(line[4*i+1]!=' '):
                stacks[i].append(line[1+4*i])
    count+=1
    for line in lines:
        if(count>0):
            count-=1
        else:
            parts=line.split(' ')
            moves=int(parts[1])
            orig=int(parts[3])-1
            dest=int(parts[5])-1
            for i in range(moves):
                stacks[dest].insert(i,stacks[orig][0])
                stacks[orig].remove(stacks[orig][0])
    top=""
    for stack in stacks:
        top+=stack[0]
    print(top)

part2()
input()
