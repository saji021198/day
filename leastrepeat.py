m=int(input())
h=list(map(int,input().split()))
count=0
k=[]
for i in range(0,m):
    n=h.count(h[i])
    k.append(n)
w=min(k)
s=k.index(w)
print(h[s])
    
