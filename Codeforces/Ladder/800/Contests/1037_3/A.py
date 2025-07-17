for _ in range(int(input())):
    n=int(input())
    l=[]
    while n != 0 :
        l.append(n%10)
        n //= 10
    print(min(l))