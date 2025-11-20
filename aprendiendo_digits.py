import math
from sklearn import datasets

misdatos = datasets.load_digits()

X= misdatos.data
y= misdatos.target

def distancia_eucli(a,b):
    suma= 0
    for i in range(len(a)):
        suma += (a[i]-b[i])**2
    return math.sqrt(suma)

distancias=[]
for i in range(len(X)):
    d= distancia_eucli(nose, X[i])
    distancias.append(d)
