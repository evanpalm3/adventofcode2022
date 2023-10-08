from dijkstra import Graph, DijkstraSPF

class Valve:
    def __init__(self):
        self.tunnelsSTR=[]
        self.tunnels=[]
        self.flowRate=0
        self.ident=""
        self.dist=[]
        
    def distance(self,valve):
        for pair in self.dist:
            if(pair[0]==valve):
                return pair[1]
        return "failed"

def powerset1(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset1(seq[1:]):
            yield [seq[0]]+item
            yield item

def powerset(l):
    r=[x for x in powerset1(l)]
    return r

dp = {}
def solve(v,t,o):
    key = (v, t, frozenset(o))
    if key in dp:
        return dp[key]

    if(t<=1):
        return 0
    m=0
    o.remove(v)
    for k in o:
        s=solve(k,t-1-v.distance(k),o.copy())
        if(s>m):
            m=s
    dp[key] = m+v.flowRate*(t-1)
    return dp[key]
    
def part2():
    lines = open('input.txt', 'r').readlines()
    valves=[]
    start=0
    for line in lines:
        line=line.replace('=',' ')
        line=line.replace(';',' ')
        parts=line.split(' ')
        ident=parts[1]
        rate=int(parts[5])
        valve=Valve()
        valve.flowRate=rate
        valve.ident=ident
        for i in range(11,len(parts)):
            valve.tunnelsSTR.append(parts[i][0:2])
        valves.append(valve)
        if(ident=='AA'):
            start=valve
    for v in valves:
        for t in v.tunnelsSTR:
            for k in valves:
                if(k.ident==t):
                    v.tunnels.append(k)
                    break
    graph=Graph()
    for v in valves:
        for t in v.tunnels:
            graph.add_edge(v,t,1)
    for v in valves:
        d=DijkstraSPF(graph,v)
        for k in valves:
            if(k==v):
                continue
            v.dist.append([k,d.get_distance(k)])
    f=[]
    for v in valves:
        if(v.flowRate==0):
            f.append(v)
    for k in f:
        valves.remove(k)
    s=powerset(valves)
    m=0
    for g in s:
        f=valves.copy()
        for k in g:
            f.remove(k)
        g.append(start)
        f.append(start)
        num=solve(start,27,g)+solve(start,27,f)
        if(num>m):
            m=num
    print(m)

part2()
input()

