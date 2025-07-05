l=[]
for _ in range(int(input())):
  q=list(map(int,input().split(" ")))
  if q[0]==1:
    l+=[q[2]]*q[1]
  else:
    if q[1] != len(l):
      print(sum(l[0:q[1]]))
      l=l[q[1]:len(l)]
    else:
      print(sum(l))
      l=[]
