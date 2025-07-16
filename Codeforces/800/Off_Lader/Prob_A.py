a,b,c,n=list(map(int,input().split(" ")))

if ((a+b-c) >= n) and (c>a or c==0) and (c>b or c==0):
    print(-1)

else:
    print(n-a-b+c)