from functools import reduce
    for _ in range(int(input())):
        n,k=list(map(int,input().split()))
        l=list(map(int,input().split()))
        if k>=2 and n>=k :
            print("yes")
        elif k==1 and n==1 :
            print("yes")
        elif k==1:
            b=[l[i]<=l[i+1] for i in range(len(l)-1)]
            print("yes" if reduce(lambda x,y : x and y, b) else "no")
        else:
            print("no")
