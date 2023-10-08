class Monkey:
    def __init__(self):
        self.items=[]
        self.op=['!', 0]
        self.div=0
        self.throw=[-1,-1]
        self.insp=0

def part2():
    lines=open('input.txt', 'r').readlines()
    monkeys=[]
    bigDiv=1
    for i in range(int((len(lines)+1)/7)):
        monke = Monkey()
        monkeys.append(monke)
        items=lines[i*7+1].split(', ')
        c=0
        for item in items:
            c+=1
            #print(item)
            if(c==1):
                monke.items.append(int(item.split(' ')[4]))
            else:
                monke.items.append(int(item))
        ops=lines[i*7+2].split(' ')
        monke.op=[ops[6],ops[7]]
        divs=lines[i*7+3].split(' ')
        monke.div=int(divs[5])
        bigDiv=bigDiv*monke.div
        throw1=lines[i*7+4].split(' ')
        throw2=lines[i*7+5].split(' ')
        monke.throw=[int(throw1[9]),int(throw2[9])]
    for i in range(10000):
        for monke in monkeys:
            for item in monke.items:
                monke.insp+=1
                if(monke.op[1]=='old\n'):
                    d=int(item)
                else:
                    d=int(monke.op[1])
                if(monke.op[0]=='*'):
                    item = item*d
                else:
                    item = item+d
                #item=int(item/3)
                item=item%bigDiv
                if(item%monke.div==0):
                    monkeys[monke.throw[0]].items.append(item)
                else:
                    monkeys[monke.throw[1]].items.append(item)
            monke.items=[]
    monkeys.sort(key=lambda x: x.insp, reverse=True)
    print(monkeys[0].insp*monkeys[1].insp)

part2()
input()