import numpy as np
a = np.array([2,1])
print(a.size)
#product of two numpy arrays
b = np.array([4,1])
print(a*b)
#Product
pr = np.dot(a,b)
#Pre-defined functions
print(pr)
print(np.max(a))
print(np.min(a))
print(np.pi)
#NP linspace.
sp = np.linspace(-2,2,num=4)
print(sp)
x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
import matplotlib.pyplot as plt 
plt.show(plt.plot(x,y))


#Embed link: https://labs.cognitiveclass.ai/tools/jupyterlab/lab/tree/labs/PY0101EN/PY0101EN-5-1-Numpy1D.ipynb
