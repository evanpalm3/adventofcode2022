def distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def part1():
    lines = open('input.txt', 'r').readlines()
    sensors=[]
    beacons=[]
    for line in lines:
        line=line.replace('=',',')
        line=line.replace(':',',')
        parts=line.split(',')
        x1=int(parts[1])
        y1=int(parts[3])
        x2=int(parts[5])
        y2=int(parts[7])
        d=distance(x1,y1,x2,y2)
        sensors.append([x1,y1,d])
        nBeacon=[x2,y2]
        b=True
        for beacon in beacons:
            if(beacon[0]==nBeacon[0] and beacon[1]==nBeacon[1]):
                b=False
                break
        if(b):
            beacons.append(nBeacon)
    ycoord=2000000
    segments=[]
    for sensor in sensors:
        if(ycoord<=sensor[1]+sensor[2] and ycoord>=sensor[1]-sensor[2]):
            if(ycoord==sensor[1]):
                segments.append([sensor[0]-sensor[2],sensor[0]+sensor[2]])
            elif(ycoord>sensor[1]):
                x1=sensor[0]-sensor[1]-sensor[2]+ycoord
                x2=sensor[1]+sensor[2]-ycoord+sensor[0]
                segments.append([x1,x2])
            else:
                x1=sensor[1]-sensor[2]-ycoord+sensor[0]
                x2=sensor[0]+sensor[2]-sensor[1]+ycoord
                segments.append([x1,x2])
    segments.sort(key=lambda x: x[0])
    merged=[]
    for segment in segments:
        if(merged==[]):
            merged.append(segment)
            continue
        last=merged[len(merged)-1]
        if(segment[0]<=last[1]):
            if(segment[1]>last[1]):
                last[1]=segment[1]
        else:
            merged.append(segment)
    count=0
    for segment in merged:
        count+=1+abs(segment[1]-segment[0])
    for beacon in beacons:
        if(beacon[1]==ycoord):
            for segment in merged:
                if(beacon[0]>=segment[0] and beacon[0]<=segment[1]):
                    count-=1
                    break
    print(count)
    
part1()
input()
