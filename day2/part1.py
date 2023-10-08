def part1():
    lines=open("input.txt", "r").readlines()
    score=0
    for line in lines:
        if(line!=""):
            opp = ord(line[0])-65
            pla = ord(line[2])-88
            if(opp==pla):
                score+=pla+4
            elif(pla==(opp+1)%3):
                score+=7+pla
            else:
                score+=pla+1
    print(score)

part1()
input()
