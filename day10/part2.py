def part2():
    lines = open("input.txt", 'r').readlines()
    cycle=1
    x=1
    idle=0
    inst=0
    im=""
    while(inst!=len(lines)):
        pos=(cycle-1)%40
        if(pos>=x-1 and pos<=x+1):
            im+='#'
        else:
            im+='.'
        if(pos==39):
            print(im)
            im=""
        
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
        
part2()
input()