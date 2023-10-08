def part2():
    lines=open("input.txt", "r").readlines()
    score=0
    for line in lines:
        if(line!=""):
            opp = ord(line[0])-65
            outcome = line[2]
            if(outcome=='X'):
                pla=opp-1
                if(pla<0):
                    pla+=3
                score+=1+pla
            elif(outcome=='Y'):
                pla=opp
                score+=4+opp
            else:
                pla=(opp+1)%3
                score+=7+pla
    print(score)

part2()
input()
