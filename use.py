import learnning 

def use(w,inp):
    teta=0.01
    yin=0
    for i in range(len(w)):
        yin += w[i]*inp[i]
    
    if yin>teta:
        y=1
    elif -teta <= yin <=teta:
        y=0
    elif -teta > yin:
        y=-1
    return y

wa=learnning.paterson("a.txt")
wb=learnning.paterson("b.txt")
wc=learnning.paterson("c.txt")
wd=learnning.paterson("d.txt")
we=learnning.paterson("e.txt")
wj=learnning.paterson("j.txt")
wk=learnning.paterson("k.txt")

input=[]
inp=[]
find = open("find.txt","r")

while True:
    x=find.readline()
    if x == "":
        break

    input.append(x.split())


for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] ==".":
            inp.append(-1)
        else:
            inp.append(1)
inp.append(1)    

if use(wa , inp) == 1:
    print("A")
elif use(wb , inp) == 1:
    print("B")
elif use(wc , inp) == 1:
    print("C")
elif use(wd , inp) == 1:
    print("D")
elif use(we , inp) == 1:
    print("E")
elif use(wj , inp) == 1:
    print("J")
elif use(wk , inp) == 1:
    print("K")