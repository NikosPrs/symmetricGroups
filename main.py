n=3
L1=[
    [],
    [3,1,2]
]
for i in range(1,n+1):
    L1[0].append(i)
print (L1)
L2=[
    [],
    [2,3,1]
]
for i in range(1,n+1):
    L2[0].append(i)
print (L2)
# L3 = L1 o L2 = id
# L4 = L2 o L1 = id
L3=[         
    [],
    []
]

for i in range(1,n+1):
    L3[0].append(i)
    j=L1[1][i-1]-1
    L3[1].append(L2[1][j])
print (L3)
L4=[         
    [],
    []
]
for i in range(1,n+1):
    L4[0].append(i)
    j=L2[1][i-1]-1
    L4[1].append(L1[1][j])
print (L4)