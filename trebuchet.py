

ans=0
with open('data1.txt','r') as f:
    lines=f.readlines()
    first=last=None
    numbers={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    for line in lines:
        n=len(line)
        i,j=0,n-1
        chosen=None
        while i<n:
            if line[i].isnumeric(): 
                chosen=int(line[i])
            elif i+2<n and line[i:i+3] in numbers:
                chosen=numbers[line[i:i+3]]
            elif i+3<n and line[i:i+4] in numbers:
                chosen=numbers[line[i:i+4]]
            elif i+4<n and line[i:i+5] in numbers:
                chosen=numbers[line[i:i+5]]
            if chosen is not None: break
            i+=1
        nextno=chosen
        chosen=None
        i=n-1
        while i>=0:
            if line[i].isnumeric(): 
                chosen=int(line[i])
            elif i+2<n and line[i:i+3] in numbers:
                chosen=numbers[line[i:i+3]]
            elif i+3<n and line[i:i+4] in numbers:
                chosen=numbers[line[i:i+4]]
            elif i+4<n and line[i:i+5] in numbers:
                chosen=numbers[line[i:i+5]]
            if chosen is not None: break
            i-=1
        ans+=10*nextno+chosen
    print(ans)