for _ in range(int(input())):
    n,k,x,y = map(int,input().split())

    a=0
    l=[]
    while a<n:
        t=(x+k)%n
        l.append(t)
        x=t
        a+=1

    if y in l:
        print("YES!")
    else:
        print("Oops! NO.")