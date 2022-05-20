import numpy as np
l = np.array([1,5,6])
u = np.zeros(7)
for i in np.nditer(l):
    u[i] = 1
    print(i)
    
print(u)