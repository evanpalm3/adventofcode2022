def part1():
    lines = open('input.txt', 'r').readlines()
    sum = 0
    for line in lines:
        s1=[]
        s2=[]
        for i in range(int(len(line)/2)):
            s1.append(line[i])
            s2.append(line[i+int(len(line)/2)])
        for k in s1:
            if(k in s2):
                val = ord(k)
                if(val>=97):
                    val-=96
                else:
                    val-=38
                sum+=val
                break
    print(sum)

part1()
input()