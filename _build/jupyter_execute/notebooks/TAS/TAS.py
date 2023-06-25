#!/usr/bin/env python
# coding: utf-8

# 
# ---
# - Prof: EL HADIQ ZOUHAIR
# - CPGE: Moulay Youssef Rabat
# - Classes: MP1, MP4, PI2
# ---

# # Les Tas binaires

# ## Tas-min et tas-max
# Un arbre binaire est dit parfait lorsque tous les niveaux hiérarchiques sont remplis sauf éventuellement le dernier, partiellement rempli de la gauche vers la droite.

# ![heap.png](heap.png)
# <center>Figure 1 – Un exemple de tas-min.</center>

# **Définition**
# - On appelle tas-max un arbre parfait étiqueté par un ensemble ordonné E tel que l’étiquette de chaque nœud autre que la racine soit inférieure ou égale à l’étiquette de son père.
# - Bien entendu, un tas-min possède la propriété opposée : l’étiquette de chaque nœud autre que la racine est supérieure ou égale à l’étiquette de son père
# 

# ### Implémentation d’un tas
# Comme tout arbre binaire, un tas peut être représenté par le type $[r,FG,FD]$, mais une autre représentation est possible en utilisant un vecteur de valeurs.
# 
# Rappelons que la numérotation **Sosa-Stradonitz** des nœuds d’un arbre binaire se définit ainsi :
# - la racine porte le numéro 0 ;
# - si un nœud porte le numéro k, son fils gauche porte le numéro 2k+1 et son fils droit le numéro 2(k + 1).
# 
# De ceci il résulte immédiatement que le père d’un nœud de numéro k porte le numéro $(k-1)//2$.
# Il est donc possible d’établir une correspondance entre l’indice k > 1 d’un tableau et la numérotation d’un nœud. 
# 
# Dans le cas d’un arbre binaire quelconque, cette représentation ne présente en général pas d’intérêt car le nombre de cases inutilisées peut être très important (dans le cas extrême d’un arbre peigne gauche, seules les cases correspondant aux puissances de 2 sont utilisées, ce qui nécessiterait un coût spatial exponentiel pour le représenter). En revanche, pour un arbre parfait, seules les cases numérotées entre 1 et n sont utilisées pour représenter un arbre de taille n.

# | 1 | 2 | 3 | 17 | 19 | 36 | 7 | 25 | 100 |
# | --|-- | -- | -- | --| -- | -- |--| --  |
# 
# Figure 2 – Une représentation tabulaire du tas-max de la figure 1.
# 

# #### Implémentation
# Un tas binaire est un arbre binaire parfait, on peut donc l'implémenter de manière compacte avec un tableau.
# 
# > - La racine se situe à l'index $0$
# > - Étant donné un nœud à l'index $i$, son fils gauche est à l'index $2i+1$ et son fils droit à $2i+2$
# > - Étant donné un nœud à l'index $i>0$, son père est à l'index $ \lfloor  \frac  {i-1}{2}   \rfloor$ (arrondi à l'entier inférieur).
# 

# ![heap_table.png](heap_table.png)

# In[1]:


def gauche(i):
    return 2*i+1

def droite(i):
    return 2*i+2
def pere(i):
    return (i-1)//2


# In[2]:


Tas_min=list(range(10))
Tas_min


# In[3]:


print(droite(0),end=' ')
print(gauche(4),end=' ')
print(droite(3),end=' ')
print(pere(9),end=' ')


# ### Opérations usuelles sur les tas

# Dans ce qui suit, nous ne prendrons en compte que des tas-max, mais il va de soit que toutes les fonctions que nous écrirons s’adaptent sans difficulté au cas des tas-min.
# ####  Préservation de la structure de tas

# Une des opérations les plus fréquentes sur les tas consiste à reconstituer la structure de tas après qu’un élément ait été modifié.
# 
# Si la nouvelle valeur de cet élément est supérieure à la précédente, il se peut que cet élément doive « monter » dans l’arbre pour reconstituer un tas ; dans le cas contraire, il se peut que cet élément ait à « descendre » dans l’arbre.

# **La montée** est plus simple : il suffit de permuter l’élément modifié avec son père tant que la structure de tas
# n’est pas reconstituée :

# In[4]:


def remonte (Tas,k):
    if k!=0:
        if Tas[k]>Tas[pere(k)]:
            Tas[k],Tas[pere(k)]=Tas[pere(k)],Tas[k]
            remonte (Tas,pere(k))


# Pour **la Percolation/ descente** , c’est un peu plus délicat : il faut permuter l’élément modifié avec le plus grand de ses fils, s’il en existe.
# 
# On introduit un paramètre supplémentaire $n$ qui indique l’indice de la première case non utilisée dans la représentation du tas.
# 
# Trois cas sont possibles : 
# - si droite(i) < n, i possède deux fils gauche(i) et droite(i) ; 
# - si n = gauche(i), i possède un seul fils gauche(i) ;
# - si gauche(i) > n, i ne possède pas de fils.

# ![entassermax.PNG](entassermax.PNG)

# In[5]:


def percolation(T,k,n=None):
    if n is None:
        n=len(T)-1
    maxf= -1 if gauche(k)>n else gauche(k) if gauche(k)==n else (gauche(k) if (T[gauche(k)]>T[droite(k)]) else droite(k))
    if maxf !=-1:
        if T[maxf]>T[k]:
            # le max des fils remonte
            T[maxf],T[k]=T[k],T[maxf]
            #on continue la descente pour l'ancien pere
            percolation(T,maxf,n)


# In[6]:


T=[1,2,3,4,5,6]
print(T)
remonte(T,5)
print(T)


# In[7]:


Tas=[1,2,3,4,5,6]
print(Tas)
percolation(Tas,0)
print(Tas)


# Le temps d’exécution de chacune des ces deux fonctions dans un tas T est un $O(h(T))$ donc un $O(log n)$, l’entier n désignant la taille du tas.

# ### construction d’un tas
# Il y a deux façons de convertir un tableau t en un tas-max. La première consiste à maintenir l’invariant : « $T[0..k]$ est un tas-max » en faisant remonter l’élément $k$ dans le tas situé à sa gauche à l’aide de la fonction monte :

# ![constTas.png](constTas.png)
# <center>Figure – Une étape de la construction d’un tas par remontée des nœuds.</center>

# In[8]:


def construire_tas1(T):
    for k in range(len(T)):
        remonte(T,k)


# In[9]:


Tas=[1,2,3,4,5,6]
print(Tas)
construire_tas1(Tas)
print(Tas)


# Dans le pire des cas, chaque remontée aboutit à la racine (c’est le cas par exemple lorsque le tableau est initialement trié par ordre croissant). Dans ce cas, le nombre de permutations effectuées est égal à la somme des profondeurs de chacun des nœuds à l’exception de la racine. Si on note $p = log (n)$ la hauteur du tas, le nombre de permutations est donc égal à :
# 
# $$\Sigma_{k=1}^{p-1}k2^k+p(n-2^p+1)=(n+1)p-2^{p+1}+2=\Theta (nlog n) $$ 

# --------

# On peut faire mieux en observant  que la deuxième moitié du tableau Tas correspond aux feuilles de l’arbre et que chacune de ces feuilles est un tas à un élément. Il suffit donc de faire descendre l’élément tk pour unir peu à peu ces différents tas, de manière à préserver l’invariant : « chaque nœud de $Tas[k..n − 1]$ est la racine d’un tas-max ».

# ![constTax2.PNG](constTax2.PNG)

# In[10]:


def creer_tas(T):
    n=len(T)-1
    for k in range(n//2,-1,-1):
        percolation(T,k,n)


# In[11]:


Tas=[1,2,3,4,5,6]
print(Tas)
creer_tas(Tas)
print(Tas)


# ## Bibliothèque python pour les Tas Min

# https://docs.python.org/3/library/heapq.html#module-heapq

# Create a Heap
# A heap is created by using python’s inbuilt library named heapq. This library has the relevant functions to carry out various operations on heap data structure. Below is a list of these functions.
# 
# - **heapify** − This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted.
# 
# - **heappush** − This function adds an element to the heap without altering the current heap.
# 
# - **heappop** − This function returns the smallest data element from the heap.
# 
# - **heapreplace** − This function replaces the smallest data element with a new value supplied in the function.

# A heap is created by simply using a list of elements with the heapify function. In the below example we supply a list of elements and the heapify function rearranges the elements bringing the smallest element to the first position.

# In[12]:


import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)


# **Inserting into heap**
# 
# Inserting a data element to a heap always adds the element at the last index. But you can apply heapify function again to bring the newly added element to the first index only if it smallest in value. In the below example we insert the number 8.

# In[13]:


# Add element
heapq.heappush(H,8)
print(H)


# In[14]:


heapq.heapify(H)
print(H)


# **Removing from heap**
# 
# You can remove the element at first index by using this function. In the below example the function will always remove the element at the index position 1.

# In[15]:


# Remove element from the heap
heapq.heappop(H)

print(H)


# **Replacing in a Heap**
# 
# The heap replace function always removes the smallest element of the heap and inserts the new incoming element at some place not fixed by any order.

# In[16]:


# Replace an element
heapq.heapreplace(H,6)
print(H)


# ## Reference
# [Jean-Pierre Becirspahic ](chttps://info-llg.fr/)
# https://info-llg.fr/option-mp/pdf/01.arbres.pdf
