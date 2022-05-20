import numpy as np 
y = np.array([1,2,3])
x = np.array([1,2])
u = [0,0]
iw = [0,0,0]
for i in range(3):
    u = (y[i] -x)**2
    u = list(u)
    iw[i] = u.index(min(u))
dic={}
for i in range(len(iw)):
    dic.update({y[i]:iw[i]})
def key_find(dic,val):
    klist=[]
    for key, value in dic.items():
        if val==value:
            klist.append(key)
    return klist 
y = np.array([[1,2],[3,4]])
print(np.sum(y,axis=0))