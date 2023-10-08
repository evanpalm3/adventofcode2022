def part1():
    lines = open('input.txt', 'r').readlines()
    line = lines[0]
    chars=[]
    index=0
    for char in line:
        chars.append(char)
        if(len(chars)>4):
            chars.remove(chars[0])
        if(len(chars)==4):
            flag=True
            for i in range(4):
                for k in range(4):
                    if(k>i):
                        if(chars[i]==chars[k]):
                            flag=False
            if(flag):
                print(index+1)
                return
        index+=1
        
part1()
input()