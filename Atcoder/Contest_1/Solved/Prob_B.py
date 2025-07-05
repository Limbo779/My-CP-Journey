l=[]
for _ in range(int(input())):
  l.append(input())

l_2=list(reversed(l))

output=[]
for i in range(len(l)):
  a=l.pop(0)
  output+=([a+j for j in l])
  
for k in range(len(l_2)):
  a=l_2.pop(0)
  output+=([a+ij for ij in l_2])
  
print(len(set(output)))

