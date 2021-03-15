n = 3
L1 = [
    [],
    [3,1,2]
]
for i in range(n):
    L1[0].append(i+1)
print(L1)
L2=[
    [],
    [2,3,1]
]
for i in range(n):
    L2[0].append(i+1)
print(L2)
L3=[     # L3 = L1 o L2 = id
    [],
    []
]
for i in range(n):
    L3[0].append(i+1)
    j=L1[1][i]
    L3[1].append(L2[1][j-1])
print(L3)
L4=[     # L4 = L2 o L1 = id
    [],
    []
]
for i in range(n):
    L4[0].append(i+1)
    j=L2[1][i]
    L4[1].append(L1[1][j-1])
print(L4)