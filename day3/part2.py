def part2():
    lines = open('input.txt', 'r').readlines()
    sum = 0
    group=[]
    count=0
    for line in lines:
        if(count<2):
            group.append(line)
            count+=1
        else:
            count=0
            for k in line:
                if(k!='\n'):
                    if(group[0].__contains__(k)):
                        if(group[1].__contains__(k)):
                            val=ord(k)
                            if(val>=97):
                                val-=96
                            else:
                                val-=38
                            sum+=val
                            group=[]
                            break
    print(sum)

part2()
input()