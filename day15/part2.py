import math

def distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def part2():
    lines = open('input.txt', 'r').readlines()
    sensors=[]
    beacons=[]
    num=0
    for line in lines:
        line=line.replace('=',',')
        line=line.replace(':',',')
        parts=line.split(',')
        x1=int(parts[1])
        y1=int(parts[3])
        x2=int(parts[5])
        y2=int(parts[7])
        d=distance(x1,y1,x2,y2)
        sensors.append([x1,y1,d,num])
        num+=1
        nBeacon=[x2,y2]
        b=True
        for beacon in beacons:
            if(beacon[0]==nBeacon[0] and beacon[1]==nBeacon[1]):
                b=False
                break
        if(b):
            beacons.append(nBeacon)
    squares=[]
    theta=math.radians(45)
    root2=math.sqrt(2)
    for sensor in sensors:
        squares.append([sensor[0]*math.cos(theta)-sensor[1]*math.sin(theta),
                        sensor[0]*math.sin(theta)+sensor[1]*math.cos(theta),
                        sensor[2]*math.sqrt(0.5),sensor[3]])
    squares.sort(key=lambda x: x[0]-x[2])
    overlap1=[]
    sep1=[]
    overlap2=[]
    sep2=[]
    tol=0.1
    for i in range(len(squares)):
        overlap1.append([])
        overlap2.append([])
        sep1.append([])
        sep2.append([])
    for i in range(len(squares)):
        overlap1.append([])
        sep1.append([])
        for k in range(i+1,len(squares)):
            l=squares[i]
            r=squares[k]
            sep=r[0]-r[2]-(l[0]+l[2])
            if(sep<0):
                overlap1[l[3]].append(r[3])
                overlap1[r[3]].append(l[3])
            else:
                if(sep>root2-tol and sep<root2+tol):
                    sep1[l[3]].append(r[3])
                    sep1[r[3]].append(l[3])
    squares.sort(key=lambda x: x[1]-x[2])
    for i in range(len(squares)):
        overlap2.append([])
        sep2.append([])
        for k in range(i+1,len(squares)):
            l=squares[i]
            r=squares[k]
            sep=r[1]-r[2]-(l[1]+l[2])
            if(sep<0):
                overlap2[l[3]].append(r[3])
                overlap2[r[3]].append(l[3])
            else:
                if(sep>root2-tol and sep<root2+tol):
                    sep2[l[3]].append(r[3])
                    sep2[r[3]].append(l[3])
    cand=[]
    for i in range(len(squares)):
        for k in overlap1[i]:
            if(k in sep2[i]):
                cand.append([i,k])
        for k in overlap2[i]:
            if(k in sep1[i]):
                o=1
                cand.append([i,k])
    cand1=[]
    for p in cand:
        u=True
        for j in cand1:
            if(j[1]==p[0] and j[0]==p[1]):
                u=False
                break
        if(u):
            cand1.append(p)
    vlines=[]
    hlines=[]
    for pair in cand1:
        sq=[]
        for square in squares:
            if(square[3]==pair[0] or square[3]==pair[1]):
                sq.append(square)
        sq.sort(key=lambda x: x[0])
        l=sq[0]
        g=l
        r=sq[1]
        sep=r[0]-r[2]-(l[0]+l[2])
        sq.sort(key=lambda x: x[1])
        k=sq[0]
        yVal=k[1]+k[2]+root2/2
        if(sep<0):
            hlines.append([[l[0]+l[2]+sep,yVal],[l[0]+l[2]-sep,yVal]])
            continue
        l=sq[0]
        r=sq[1]
        sep=r[1]-r[2]-(l[1]+l[2])
        xVal=g[0]+g[2]+root2/2
        vlines.append([[xVal,l[1]+l[2]+sep],[xVal,l[1]+l[2]-sep]])
    points=[]
    for hline in hlines:
        for vline in vlines:
            if(hline[0][1]<vline[1][1]+tol and hline[0][1]>vline[0][1]-tol):
                if(vline[0][0]<hline[1][0]+tol and vline[0][0]>hline[0][0]-tol):
                    points.append([vline[0][0],hline[0][1]])
    tpoints=[]
    for p in points:
        theta=math.radians(-45)
        x=p[0]*math.cos(theta)-p[1]*math.sin(theta)
        y=p[0]*math.sin(theta)+p[1]*math.cos(theta)
        tpoints.append([int(x+tol),int(y+tol)])
    x=-1
    y=0
    for p in tpoints:
        if(p[0]<0 or p[0]>4000000):
            continue
        if(p[1]<0 or p[1]>4000000):
            continue
        k=True
        for s in sensors:
            if(distance(p[0],p[1],s[0],s[1])<=s[2]):
                k=False
        if(k):
            x=p[0]
            y=p[1]
            break
    if(x==-1):
        print("failed, check edge case")
        return
    print(x*4000000+y)

part2()
input()
