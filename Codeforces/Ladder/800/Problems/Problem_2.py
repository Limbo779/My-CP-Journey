for _ in range(int(input())):
    n,x = list(map(int,input().split()))
    l=list(map(int,input().split()))
    dif=[l[0]]+[l[i]-l[i-1] for i in range(1,len(l))]+[2*(x-l[-1])]
    print(max(dif))