import numpy as np
import matplotlib.pyplot as plt

d1=lambda A,B: sum([abs(a-b) for a,b in zip(A,B)])
d2=lambda A,B: np.sqrt(sum([(a-b)**2 for a,b in zip(A,B)]))
d_inf=lambda A,B: max([abs(a-b) for a,b in zip(A,B)])
d2_np=lambda A,B: np.sqrt(sum((A-B)**2))
d1_np=lambda A,B: sum(abs(A-B))
d_inf_np=lambda A,B: max(abs(A-B))
d1_matrixe=lambda M1,M2:max([d1(L) for L in M1-M2])


##Some additional functions
def partitionner(D,Y):
    TestData,TestTarget,LearningData,LearningTarget=[],[],[],[]
    for i in range(len(Y)):
        if i%5==0:
            TestData.append(D[i]);TestTarget.append(Y[i])
        else:
            LearningData.append(D[i]);LearningTarget.append(Y[i])
    return TestData,TestTarget,LearningData,LearningTarget


def convert_to_np_arrays(Listes):
    return tuple(list(map(lambda table:np.array(table),Listes)))

def distances (y , D,d=d2) :
    """
    entrée :
        D = liste d'objets (élément de R^n) de longueur N
        y = objet (élément de R^n)
        on dispose d'une fonction d
        qui mesure la distance entre objets
    sortie :
        lD = liste de float= liste des distances d(y,xk ) pour k dans [|1 , N |]
    """
    return np.array([d(y,x) for x in D])
    

def KNN(Distaces,k):
    """
    entrée :
            Distaces = liste de float
               = liste des distances entre l'objet à placer 
               y et chacun des objets de la liste d'apprentissages
            K = int = nombre de voisins à prendre en compte 
    sortie : lKNN = liste de int de longueur K
      = liste des indices des K plus proches voisins .
"""
    return np.argsort(Distaces)[:k]

def KNN_version2(Distances,k):
    triee=sorted(enumerate(D),key=lambda e:e[1])
    return np.array([e[0] for e in triee][:k])

def Compter(TargetValues):
    compteur={}
    for e in TargetValues:
        if e not in compteur:
            compteur[e]=1
        else:
            compteur[e]+=1
    return compteur

def Plus_commun(compteur):
    return max(compteur,key=lambda e:compteur[e])

def predict(y,LearningData,LearningTarget,d=d2_np,k=11):
    Ditanceslist=distances(y,LearningData,d)
    voisins=KNN(Ditanceslist,k)
    return Plus_commun(Compter(LearningTarget[voisins]))
    #return Counter(LearningTarget[voisins]).most_common()[0]

def ConfusionMatrix(TestData,TestTarget,model):
    LearningData,LearningTarget,d,k=model
    types=list(set(TestTarget))
    typesDict={e:i for i,e in enumerate(types)}
    n=len(types)
    matrice=np.zeros((n,n))
    for i in range(len(TestData)):
        p=predict(TestData[i],LearningData,LearningTarget,d,k)
        matrice[typesDict[TestTarget[i]],typesDict[p]]+=1
    return matrice


