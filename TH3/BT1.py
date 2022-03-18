import math

def vector_text(T, d):
    d = d.split()
    v = []
    for t in T:
        v.append(d.count(t))
    return v
def vector_donvi(v):
    v1 = 0
    for i in v:
        v1 += i*i
    long_v = math.sqrt(v1)
    for i in v:
        v[i] = v[i]/ long_v
    return v

def cosin(v1 , v2):
    v3 = vector_donvi(v2)
    cos = 0
    for i in range(len(v1)):
        cos += v1[i]*v3[i]
    return cos

text1 = "This is a foo bar sentence ."
text2 = "This sentence is similar to a foo bar sentence ."
t = "This is bar" 
v1 = vector_text(t,text1)
v2 = vector_text(t,text2)

print("cosin: ", cosin(v1,v2))
