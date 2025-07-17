a,b,c,n=list(map(int,input().split(" ")))

if ((a+b-c) < n) and (c==0 or c<=min(a,b)) :
    print(n-a-b+c)

else:
    print(-1)
