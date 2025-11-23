from sklearn import datasets
import numpy as np


datos = datasets.load_digits()


#distintos digitos procesados para ser comparados de varias formas
X= datos.data
y= datos.target

data = np.loadtxt("numeros.csv", delimiter=",", skiprows=1)

digitos = data[:, :64]

#Flatten
vectores = [mat.flatten() for mat in digitos]

def distancia_eucli(a,b):
    suma= 0
    for i in range(len(a)):
        suma += (a[i]-b[i])**2
    return suma**0.5

indicevector=0
#Distancias acumuladas por digito
distancia_Todos=[]
for digito in range(len(vectores)):
    distancia1=[]
    #distancias por digito
    for i in range(len(X)):
        d=distancia_eucli(vectores[digito],X[i])
        distancia1.append(d)
    distancia_Todos.append(distancia1)


reales = [i for i in range(10) for _ in range(6)]

for dig_index in range(len(distancia_Todos)):
    #el digito en cuestion y sus distancias
    dig=distancia_Todos[dig_index]
    #indices de la lista
    indices = list(range(len(dig)))

    for i in range(len(indices)):
        for j in range(i+1, len(dig)):
            if dig[j]<dig[i]:
                temp=indices[i]
                indices[i]=indices[j]
                indices[j]=temp
    #en las listas ordenadas
    vecinos= indices[:3]

    #numeros reales
    targets = [int(y[i]) for i in vecinos]
    d={}
    for i in range(len(targets)):
        if targets[i] not in d:
            d[targets[i]] = 1
        else:
            d[targets[i]] += 1

    vecs=[]
    repes=[]
    for v,r in d.items():
        vecs.append(v)
        repes.append(r)

    for i in range(len(repes)):
        if repes[i]==max(repes):
            resultado=vecs[i]
    print(f"Numero real: {reales[dig_index]}")
    print(f"Sus vecinos: {targets}")
    print(f"Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número {resultado}")


