from pickle import FALSE
from numpy import double
import math 


def calculateCG(list):
    newList = []
    CG = 0
    index=0
    for i in list:
        index +=1
        id = i[0]
        rel = i[1]
        CG += rel
        if(index >1):
            loga = math.log2(index)
        else:
            loga = ''
        tup = (id,rel,CG,loga)
        newList.append(tup)
    return newList
def calculateDCG(list):
    newList = []
    index = 0
    for i in list:
        index +=1
        id = i[0]
        rel = i[1]
        CG = i[2]
        loga = i[3]
        if(loga == ''):
            DCG = 1
            temp = 0
        else:
            temp += rel/loga
            DCG = 1+temp
        tup = (index,id,rel,CG,loga,DCG)
        newList.append(tup)
    return newList
def calculateIDCG(newList):
    newDCG = calculateCG(newList)
    newList = []
    index = 0
    for i in newDCG:
        index +=1
        id = i[0]
        rel = i[1]
        CG = i[2]
        loga = i[3]
        if(loga == ''):
            IDCG = 1
            temp = 0
        else:
            temp += rel/loga
            IDCG = 1+temp
        tup = (index,id,rel,CG,loga,IDCG)
        newList.append(tup)
    return newList
def calculateNDCG(listDCG,listIDCG):
    newList = []
    for i in listDCG:
        for j in listIDCG:
            if(i[0] == j[0]):
                id = i[1]
                rel = i[2]
                DCG = i[5]
                IDCG = j[5]
                NDCG = DCG/IDCG
                tup = (id,rel,DCG,IDCG,NDCG)
                newList.append(tup)
    return newList

list = [(588,1),(589,0.6),(576,0),(590,0.8),(986,0),(592,1),(984,0),(988,0),(578,0),(985,0),(103,0),(591,0),(772,0.2),(990,0)]
listCG = calculateCG(list)
listDCG = calculateDCG(listCG)
def takeSecond(elem):
    return elem[1]
list.sort(key=takeSecond, reverse= True)
listIDCG = calculateIDCG(list)
listNDCG = calculateNDCG(listDCG,listIDCG)
for i in listNDCG:  
    print(i)