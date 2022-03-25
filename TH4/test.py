import math
def cg(li, n):
    cgn = 0
    li_cgn = []
    for i in range(n):
            cgn += li[i][1]
            li_cgn.append(cgn)
    return li_cgn
def dcg(li , n):
    li_dcg = []
    summ = 0
    for i in range(n):
        if(i == 0):
            li_dcg.append(li[i][1])
        else:
            summ += li[i][1]/math.log2(i+1)
            li_dcg.append(li[0][1] + summ)
    return li_dcg
"""
n = int(input("Nhap n: "))
tup 🙁)
li = []
for i in range(n):
    mavb = input("Nhap ma van ban:")
    rel = input("Nhap do phu hop van ban:")
    tup = (mavb,rel)
    li.append(tup)
"""
n = 14
li = [(1,1),(2,0.6),(3,0),(4,0.8),(5,0),(6,1),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0.2),(14,0)]
print("Khi chua chuan hoa: \n")
print(cg(li,n), "\n")
print(dcg(li, n),"\n")
Dcg = dcg(li, n)

li.sort(reverse = True ,key=lambda tup: tup[1])
print("Sau khi chuan hoa: \n")
print(cg(li,n), "\n")
print(dcg(li, n),"\n")

cgn = cg(li,n)
idcg = dcg(li,n)
ndcg = []
for i in range(n):
    ndcg.append(Dcg[i]/idcg[i])
print("NDCG: ", ndcg)