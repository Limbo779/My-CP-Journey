for _ in range(int(input())):
  n=int(input())
  l=list(map(int,input().split(" ")))
  l_abs=list(map(abs,l))
  st=min(l_abs)
  en=max(l_abs)
  
  print(l,l_abs)

  if l == l_abs:
    r=(en/st)**(1/(n-1))
  else:
    r=(en/st)**(1/(n-1))*(-1)
  print("Yes" if sum(l)==((st*((r**n)-1))/(r-1)) else "No")
