def part1():
    lines = open("input.txt", 'r').readlines()
    markers=[20,60,100,140,180,220]
    cycle=1
    x=1
    idle=0
    inst=0
    signal=0
    while(inst!=len(lines)):
        for mark in markers:
            if(cycle==mark):
                signal+=cycle*x
        
        words=lines[inst].split(' ')
        if(idle>0):
            idle-=1
            if(idle==0):
                x+=int(words[1])
                inst+=1
        else:
            if(words[0]=='addx'):
                idle+=1
            else:
                inst+=1
        cycle+=1
    print(signal)
    
part1()
input()