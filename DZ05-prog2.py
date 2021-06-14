def parinepar(x):
    print("Parni:")
    br=0
    while(br<x):
        yield br
        br+=2
    print("Neparni:")
    br=1
    while(br<x):
        yield br
        br+=2
        
for i in parinepar(40):
    print(i)
