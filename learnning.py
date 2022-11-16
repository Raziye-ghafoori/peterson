

def paterson (f):
    teta=0.01
    A=0.2
    w=[]

    for i in range(64):
        w+=[0]

    while True:
        ch=0
        file=open(f,"r")
        while True:
            inp=[]
            y_in=0
            x=file.readline()
            if x=="":
                break

            h=x.split()
            for i in range(len(h)):
                inp.append(float(h[i]))
            inp.insert(len(h)-1,1)

            for i in range(len(w)):
                y_in += w[i] * float(inp[i])  
            
            if y_in > teta:
                y=1   
            elif -teta <= y_in <= teta:
                y=0
            elif y_in < -teta:
                y=-1

            if y !=  inp[len(inp)-1]:
                for i in range(len(w)):
                    w[i] += A*inp[len(inp)-1]*inp[i]
                
                ch=1

        file.close()
        if ch == 0:
            break

    return w