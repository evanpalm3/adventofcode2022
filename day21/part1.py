class Oper:
    def __init__(self):
        self.p1=0
        self.p2=0
        self.op=0
        self.val='u'

memo={}
def calc(op):
    if(op.val!='u'):
        return op.val
    l=calc(memo[op.p1])
    r=calc(memo[op.p2])
    if(op.op=='+'):
        return l+r
    elif(op.op=='-'):
        return l-r
    elif(op.op=='*'):
        return l*r
    elif(op.op=='/'):
        return int(l/r)
    else:
        print('no operation')

def part1():
    lines=open('input.txt','r').readlines()
    for line in lines:
        parts=line.split(' ')
        op=Oper()
        ident=parts[0][0:4]
        if(len(parts)==4):
            op.p1=parts[1]
            op.p2=parts[3][0:4]
            op.op=parts[2]
        else:
            op.val=int(parts[1])
        memo[ident]=op
    print(calc(memo['root']))

part1()
input()
