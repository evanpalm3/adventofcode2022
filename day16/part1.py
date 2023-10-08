from dijkstra import Graph, DijkstraSPF

class Valve:
    def __init__(self):
        self.tunnelsSTR=[]
        self.tunnels=[]
        self.flowRate=0
        self.ident=""
        self.open=False
        self.dist=[]
        
    def distance(self,valve):
        for pair in self.dist:
            if(pair[0]==valve):
                return pair[1]
        return "failed"

def solve(v,t,o):
    if(t<=1):
        return 0
    m=0
    o.remove(v)
    for k in o:
        s=solve(k,t-1-v.distance(k),o.copy())
        if(s>m):
            m=s
    return m+v.flowRate*(t-1)
    
def part1():
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
    valves.append(start)
    print(solve(start,31,valves))

part1()
input()

