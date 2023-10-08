class nFile:
    def __init__(self):
        self.name = ""
        self.size = 0

class nDir:
    def __init__(self):
        self.prev = None
        self.size = 0
        self.dirs = []
        self.files = []
        self.name=""

def buildDir():
    lines = open('input.txt', 'r').readlines()
    root = nDir()
    root.name="root"
    current = root
    for line in lines:
        words = line.split(' ')
        if(words[0]=='$'):
            if(words[1]=='cd'):
                if(words[2]=='/'):
                    current=root
                    continue
                elif(words[2]=='..\n'):
                    current=current.prev
                    continue
                else:
                    for dir1 in current.dirs:
                        if(dir1.name==words[2]):
                            current=dir1
                            break
                    continue
            elif(words[1]=='ls'):
                continue
            else:
                continue
        elif(words[0]=='dir'):
            newDir = nDir()
            newDir.prev=current
            newDir.name=words[1]
            current.dirs.append(newDir)
            continue
        else:
            newFile = nFile()
            newFile.size=int(words[0])
            newFile.name=words[1]
            current.files.append(newFile)
            temp=current
            temp.size+=newFile.size
            while(temp.prev!=None):
                temp=temp.prev
                temp.size+=newFile.size
            continue
    return root

def traverse(current, layer):
    text=""
    for i in range(layer):
        text+="   "
    print(text+"dir:"+current.name)
    text+="   "
    for file in current.files:
        print(text+"file:"+file.name)
    for dir1 in current.dirs:
        traverse(dir1, layer+1)
    

def getList1(current, list1):
    if(current.size<=100000):
        list1.append(current)
    for dir1 in current.dirs:
        getList1(dir1, list1)

def getList2(current, list1, need):
    if(current.size>=need):
        list1.append(current)
    for dir1 in current.dirs:
        getList2(dir1, list1, need)
    
def part1():
    root = buildDir()
    dirList = []
    getList1(root, dirList)
    sum1=0
    for dir1 in dirList:
        sum1+=dir1.size
    print(str(sum1))
    
part1()
input()
