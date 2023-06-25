#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


# In[2]:


#https://www.youtube.com/watch?v=0p0o5cmgLdE


# Dans ce chapitre, on voit deux algorithmes pour l’intelligence artificielle : les k plus
# proches voisins (KNN k nearest neighbors) et les k-moyennes (k means).

# # Algorithme KNN: Cours

# ## Classification supervisée

# - On considère le problème suivant : on dispose N objets sur lesquels on a mesuré différentes valeurs.\
# Les mêmes mesures ont été faites sur chacun des objets.
# - La valeur de N est très grande.
# - Ces objets se répartissent selon T classes, avec T petit. On sait dans quel classe va chaque objet que l’on a mesuré.
# - Maintenant, on ajoute un nouvel objet sur lequel on a fait les mêmes mesures. 
# - On souhaite lui associer une classe.
# - De quelle classe est-il le plus proche ?

# On parle ainsi **D’APPRENTISSAGE SUPERVISÉ** . En effet, on apprend sur un jeu des données déjà classées comment classer les nouvelles données.

# *Exemple 1.*
# - Ce type d’algorithme est très utilisé en intelligence artificielle particulièrement dans le commerce en ligne.
# - On a des informations sur N personnes (âge, sexe, habitude de navigation, etc.). On a classé leurs centres d’intérêts selon T types.
# - On peut alors proposer automatiquement à un nouvel individu des publicités adap-
# tées en le classant automatiquement.

# *Exemple 2.*
# - Pour faire des diagnostics automatiques, On dispose de mesures médicales sur N individus pour lesquels on sait si il y a ou pas une tumeur cancéreuse, c'-à-d que l’on a répartis dans deux classes : malade / sain.
# - À partir de ces données, on peut déterminer automatiquement si un individu doit être considéré comme malade ou sain.

# ## La notion de distance:
# - Pour donner un sens à la classe la plus proche, cela suppose a minima de choisir une manière de mesurer les écarts entre les objets, c-à-d d’avoir une distance sur les mesures associées à aux objets.
# - Cela n’est pas du tout évident. D’autant plus que les mesures peuvent prendre
# diverses formes.
# - Le choix de la distance est donc critique pour la classification.

# In[3]:


d1=lambda A,B: sum([abs(a-b) for a,b in zip(A,B)])
d2=lambda A,B: np.sqrt(sum([(a-b)**2 for a,b in zip(A,B)]))
d_inf=lambda A,B: max([abs(a-b) for a,b in zip(A,B)])
d2_np=lambda A,B: np.sqrt(sum((A-B)**2))
d1_np=lambda A,B: sum(abs(A-B))
d_inf_np=lambda A,B: max(abs(A-B))


# ## Principe de l’algorithme
# **Mathématiquement**, 
# - On dispose donc d’un ensemble $E$ assez complexe (l’ensemble des mesures), $E$ est muni d’une distance $d$.
# - On dispose d’un ensemble C de classe de cardinal T .
# - On dispose donc de N éléments de $E \times C$ (les mesures faites sur les objets et les classes associées). On les notes $(x_j , c_j)_{j\in [1, N]}$ . 
# - Ainsi, $x_j$ est la liste des mesures faites sur l’objet $j$, et $c_j$ la classe associée.
# - **Problème** On considère de plus un élément y de E, non classé et on veut lui associer une classe.
# 
# **Exemple :**
# Comme problème jouet, on considère donc que $E = \mathbb{R}^n$ et que l’on prend la distance
# euclidienne. 

# L’algorithme des KNN consiste à :
# - mesurer les distance $d(y, x_j )$ pour $j ∈ [|1, N|]$,
# - déterminer les k plus proches voisins de y. Les k éléments les plus proches de
# y sont notés : $x_{i_1} , x_{i_2} , . . . , x_{i_k}$ .
# - Choisir pour classe de y la classe la plus fréquente parmi celles de $(x_{i_1} , x_{i_2} , . . . , x_{i_k} )$
# 
# 
# Le choix du paramètre k (nombre de voisins que l’on prend en compte) est critique.\
# Il n’est pas facile de régler ce paramètre et de l’interpréter.\
# D’autre part, on peut avoir plusieurs classes avec le même effectif parmi les k voisins.\
# Dans ce cas, l’algorithme ne permet pas de conclure et on attribue généralement arbitrairement une classe au nouvel objet y.

# ## Mise en place de chaque étape

# ### Mesure des distances

# On commence donc par créer une liste des distances : $d(y, x_j )$ pour $j \in [[1, N]]$.

# In[4]:


def Distances(y ,LearningData,d=d2) :
    """
    entrée :
        lX = liste d'objets ( é l é ment de R^n) de longueur N
        y = objet ( é l é ment de R^n)
        on dispose d'une fonction d
        qui mesure la distance entre objets
    sortie :
        lD = liste de float= liste des distances d(y,xk ) pour k dans [|1 , N |]
    """
    return [d(y,x) for x in LearningData]
    


# ### Déterminer les k plus proches voisins
# Ensuite, il s’agit de déterminer les k plus proches voisins.\
# Pour cela, on se contente d’utiliser l’algorithme de tri rapide en etulisant la fonction **sorted**.

# Ici, on voit que l’on veut les indices des éléments les plus proches, pas les valeurs.\
# En effet, ce n’est pas trier les distances qui nous intéressent mais trier les points.\
# C'est pour cette raison nous n'allos pas utiliser **sorted** directement sur les distances mais nou allons utiliser la fonction **np.argsort** qui retourne la liste des indices des elements qui rendent la liste des distances une liste triée.

# In[5]:


## Exemple 
distances=[5,10,9,11,0.3]
indices=np.argsort(distances)
print("les distances: ",distances)
print("les indices: ",indices)
print("{} est l'indice de {} dans la liste distances, ce qui représente la distance minimale,\naisni {} est l'indice de  la distance maximale qui est {}".format(indices[0],distances[indices[0]],indices[-1],distances[indices[-1]]))


# In[6]:


def KNN(Ditanceslist,k):
    """
    entrée :
            Ditanceslist = liste de float
               = liste des distances entre l'objet à placer 
               y et chacun des objets de la liste d'apprentissages
            k = int = nombre de voisins à prendre en compte 
    sortie : lKNN = liste de int de longueur K
      = liste des indices des K plus proches voisins .
"""
    return np.argsort(Ditanceslist)[:k]


# In[7]:


def KNN_version2(Ditanceslist,k):
    triee=sorted(enumerate(Ditanceslist),key=lambda e:e[1])
    return [e[0] for e in triee][:k]


# 

# ### Choisir la classe la plus fréquente
# Pour déterminer la classe la plus fréquente, il faut compter combien de fois est présente chaque classe.
# 
# Pour cela, on parcourt les k plus proches avec un compteur de longueur T (le nombre de classe). 
# 
# Pour chaque élément lu, on incrémente le compteur correspondant.

# In[8]:


def Compter(TargetValues):
    compteur={}
    for e in TargetValues:
        if e not in compteur:
            compteur[e]=1
        else:
            compteur[e]+=1
    return compteur


# Ensuite, un simple algorithme de recherche de maximum donne la classe la plus fréquente.

# In[9]:


def Plus_commun(compteur):
    max(compteur,key=lambda e:compteur[e])


# ### Prédire la Sortie d'une nouvelle donnée

# In[10]:


def predict(y,LearningData,LearningTarget,d=d2_np,k=11):
    Ditanceslist=distances(y,LearningData,d)
    voisins=KNN(Ditanceslist,k)
    return Plus_commun(Compter(LearningTarget[voisins]))
    #return Counter(LearningTarget[voisins]).most_common()[0]
    #


# ### Matrice de confusion
# La matrice de confusion permet de mesurer la qualité du système de classification.\
# Pour tester la qualité, on prend M objets dont on connaît la classification.\
# Cette classification est qualifiée de certaine.\
# On applique l’algorithme à chacun de ses M objets et on note la classification obtenue (dite classification estimée).\
# On met ces résultats dans une matrice : chaque ligne de la matrice correspond à une classe certaine, chaque colonne a une classe estimée. Ainsi ligne i et colonne j on met le nombre d’éléments qui ont été classifiée dans la classe j alors qu’ils sont dans la classe i.\
# Si la classification était parfaite, alors seule la diagonale aurait des éléments non nuls.\
# On considère qu’une classification est de qualité lorsque chaque ligne contient 95% de ses valeurs sur l’élément diagonal.

# In[11]:


def ConfusionMatrix(TestData,TestTarget,model):
    LearningData,LearningTarget,d,k=model
    types=list(set(TestTarget))
    n=len(types)
    matrice=np.zeros((n,n))
    for i in range(len(TestData)):
        p=predict(TestData[i],LearningData,LearningTarget,d,k)
        matrice[TestTarget[i],p]+=1

