def part2():
    lines = open('input.txt', 'r').readlines()
    line = lines[0]
    chars=[]
    index=0
    for char in line:
        chars.append(char)
        if(len(chars)>14):
            chars.remove(chars[0])
        if(len(chars)==14):
            flag=True
            for i in range(14):
                for k in range(14):
                    if(k>i):
                        if(chars[i]==chars[k]):
                            flag=False
            if(flag):
                print(index+1)
                return
        index+=1
        
part2()
input()