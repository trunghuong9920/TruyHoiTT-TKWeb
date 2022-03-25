from pickle import FALSE
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
        loga = math.log2(index)
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
        if(loga == 0):                          #văn bản 2->n
            temp = 0
        else:
            temp += rel/loga
        DCG = list[0][1]+temp                   #list[0][1] = rel(1)
        tup = (index,id,rel,CG,loga,DCG)
        newList.append(tup)
    return newList

def calculateIDCG(newList):
    newDCG = calculateCG(newList)           #Tính lại CG, log
    newIDCG = calculateDCG(newDCG)
    return newIDCG
def calculateNDCG(listDCG,listIDCG):
    newList = []
    for i in listDCG:
        for j in listIDCG:
            if(i[0] == j[0]):
                index = i[0]
                id = i[1]
                rel = i[2]
                DCG = round(i[5],2)
                IDCG = round(j[5],2)
                NDCG = round(DCG/IDCG,2)
                tup = (index,id,rel,DCG,IDCG,NDCG)
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
