faces=[[.5,0,0],[0,.5,0],[0,0,.5],[-.5,0,0],[0,-.5,0],[0,0,-.5]]
       
def intersection(a,b):
    c=[]
    for k in a:
        if(k in b):
            c.append(k)
    return c

def part1():
    lines = open('input.txt', 'r').readlines()
    drop1=set()
    drop2=set()
    blocks=0
    for line in lines:
        blocks+=1
        parts=line.split(',')
        cube=int(parts[0]),int(parts[1]),int(parts[2])
        x,y,z=cube
        for face in faces:
            k=x+face[0],y+face[1],z+face[2]
            if(k in drop1):
                drop2.add(k)
            else:
                drop1.add(k)
    sa=6*blocks-2*len(drop2)
    print(sa)
    
part1()
input()
