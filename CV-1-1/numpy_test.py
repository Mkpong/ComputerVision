import numpy as np

a = np.array([1,3,2,4,5,6,7,0])
print(a)
print(type(a))
print(a.shape)
a.sort()
print(a)

b = np.array([-4.3,-2.4,12.5,6.3,1,-1.2])
b.sort()
print(b)

c = np.array(["one" , "two" , "three" , "four"])
c.sort()
print(c)
