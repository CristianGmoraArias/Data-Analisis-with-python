import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")


    calculations = dict()
    mea,variance,standard_deviation,maximo,minimo,suma = [],[],[],[],[],[]
    matriz = np.array(list).reshape(3,3)

    #Mean Calculate
    columnas = np.mean( matriz , axis = 0).tolist()       
    filas = np.mean( matriz , axis = 1).tolist()
    total = np.mean(matriz)
    mea.append(columnas)
    mea.append(filas)
    mea.append(total)
    calculations['mean'] = mea

    #Variance Calculate
    columnas = np.var( matriz , axis = 0).tolist()
    filas = np.var( matriz , axis = 1).tolist()
    total = np.var(matriz)
    variance.append(columnas)
    variance.append(filas)
    variance.append(total)
    calculations['variance'] = variance

    #Standar deviation
    columnas = np.std( matriz , axis = 0).tolist()
    filas = np.std( matriz , axis = 1).tolist()
    total = np.std(matriz)
    standard_deviation.append(columnas)
    standard_deviation.append(filas)
    standard_deviation.append(total)
    calculations['standard deviation'] = standard_deviation

    #max
    columnas = np.max( matriz , axis = 0).tolist()
    filas = np.max(matriz , axis = 1).tolist()
    total = np.max(matriz)
    maximo.append(columnas)
    maximo.append(filas)
    maximo.append(total)
    calculations['max'] = maximo

    #min
    columnas = np.min( matriz , axis = 0).tolist()
    filas = np.min( matriz , axis = 1).tolist()
    total = np.min(matriz)
    minimo.append(columnas)
    minimo.append(filas)
    minimo.append(total)
    calculations['min'] = minimo

    #sum
    columnas = np.sum( matriz , axis = 0).tolist()
    filas = np.sum( matriz , axis = 1).tolist()
    total = np.sum(matriz)
    suma.append(columnas)
    suma.append(filas)
    suma.append(total)
    calculations['sum'] = suma


    return calculations