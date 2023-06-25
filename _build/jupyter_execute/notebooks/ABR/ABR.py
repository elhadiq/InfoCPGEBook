#!/usr/bin/env python
# coding: utf-8

# # Arbres Binaires de Recherche

# <div class="alert alert-info" role="alert"> 
# 
# **Indication**:  Concernant les cellules qui contiens des théorèmes enlever le commenatire (< !-- -- >) pour visualiser la preuve apres avoir essayer le prouvé vous meme  </div>

# In[1]:


import numpy as np
import random


# --------------

# Un arbre binaire de recherche {cite}`JPBABR` (en abrégé : ABR) permet l’implémentation sous forme d’arbre binaire de certaines structures de données stockant des éléments formés d’une clé et d’une valeur, tels les dictionnaires 7.<br>
# Nous allons donc considérer un ensemble ordonné de clés $C$ ainsi qu’un ensemble de valeurs $V$, et utiliser des arbres binaires étiquetés par $E = C × V.$<br>
# Les arbre binaire de recherche supportent nombre d’opérations qu’on utilise dans les structures de données, en particulier :<br>
# - la recherche d’un valeur associée à une clé donnée ;
# - la recherche de la valeur associée à la clé maximale (ou minimale) ;
# - la recherche du successeur d’une clé c, c’est à dire la valeur associée à la plus petite des clés strictement supérieures à c ;
# - la recherche du prédécesseur d’une clé ;
# - et bien sûr l’insertion ou la suppression d’un nouveau couple clé/valeur.

# ![abr.png](abr.png)
# 
# Figure 1 – Un exemple d’arbre binaire de recherche (seules les clés ont été représentées)

# **Définition.**<br>
# un arbre binaire $A$ est un arbre binaire de recherche s’il est vide ou égal à $[(c,v),Fg, Fd]$ où :
# >- $Fg$ et $Fd$ sont des arbres binaires de recherche ;
# >- toute clé de $Fg$ est inférieure (ou égale ) à $c$ ;
# >- toute clé de $Fd$ est supérieure (ou égale) à $c$.

# Autrement dit, A est un arbre binaire de recherche lorsque tout nœud de A est associé à une clé supérieure ou 
# égale à toute clé de son fils gauche, et inférieure ou égale à toute clé de son fils droit.

# <div class="alert alert-success" role="alert">
# 
# **Theorème.** Lors du parcours infixe d’un arbre binaire de recherche, les clés sont parcourues par ordre croissant.<br><br>
#     
#     
# 
# 
# **Preuve.** On **procède** par induction :
# - si A = [ ], il n’y a rien à prouver ;
# - si A = [x,Fg,Fd], on suppose que les parcours infixes de Fg et de Fd se font par ordre de clés croissantes.
# Sachant que toute clé de Fg est inférieure à la clé de x et toute clé de Fd supérieure à cette dernière, le parcours $$Fg \rightarrow x\rightarrow Fd$$ est bien effectué par ordre croissant de clé.
# -->
# </div>
# 
# 

# ## Insertion et suppression

# ### 1. Insertion et suppression dans un arbre binaire de recherche quelconque

# #### Insertion 

#  Pour insérer le couple $(k;u) \in C×V$ dans l’arbre $A$ on procède ainsi :
# > - si $A = [ ]$, on retourne l’arbre $((k,u),[],[])$ ;
# > - si $A = [(c,v),Fg,Fd]$ alors :
# >     -  si $c = k$ on remplace  le couple $(c,v)$par $(k,u)$et on insère $(c,v)$dans $Fg$ou $Fd$;
# >     - si $c > k$ on insère $(k,u)$ dans $Fg$;
# >     - si $c < k$ on insère $(k,u)$ dans $Fd$

# In[2]:


def insertion_feuille(A,paire):
    if A==[]:
        A.extend([paire,[],[]])
    elif paire[0]<=A[0][0]:
        insertion_feuille(A[1],paire)
    else:
        insertion_feuille(A[2],paire)


# In[3]:


def remplire(A,L):
    for paire in L:
        insertion_feuille(A,paire)


# In[4]:


def initialiser():
    random.seed(0)#Pour avoir les meme valeurs aleatoires
    L=[random.randint(0,20) for _ in range(8)]
    L=[(e,"v"+str(e)) for e in L]
    #print("-->".join([str(p) for p in  L]))
    A=[]#Initialisation par liste vide.
    remplire(A,L)
    #print(L)
    return A,L


# In[5]:


A,L=initialiser()
print(A)


# Cette fonction d’insertion à un coût en $O(h(A))$.

# ### Suppression

# #### Supprission de la valeur minimale

# Nous aurons besoin d’une fonction qui prend en argument un arbre $A$ et retourne le couple $(m;A')$ formé d’un élément m de clé minimale et de l’arbre $A' = A\backslash  \{m\}$ :
# > - Si A=[ ]: Alors rien à supprimer
# > - Si Fg=[ ] alors supprimer la racine et remplacer l'arbre A par Fd.
# > - Sinon supprimer le couple minimale à partir de l'arbre gauche.

# In[6]:


def supprime_min(A):
    if A==[]:
        return None
    if A[1]==[]:
        droped=A[0]
        A[:]=A[2]
        return droped
    return supprime_min(A[1])


# La suppression d’une clé $k$ dans un arbre binaire de recherche consiste à supprimer le couple $(k;v)$ situé à la profondeur minimale dans l’arbre $A = [(c;v);Fg;Fd].$ On procède ainsi :
# > - si $k < c$, on supprime un élément de clé k dans Fg ;
# > - si $k > c$, on supprime un élément de clé k dans Fd ;
# > - si $k = c$, alors :
# >    - si $Fg = [ ]$ on renvoie $Fd$ ;
# >    - si $Fd = [ ]$ on renvoie $Fg$ ;
# >    - sinon, on supprime de $Fd$ un élément $m$ de clé minimale pour obtenir $Fd'$ et on retourne [m, Fg, Fd' ].

# La suppression d’une clé k se réalise alors ainsi :

# In[7]:


def supprimer(A,k):
    if A==[]:
        return None
    if k<A[0][0]:
        return supprimer(A[1],k)
    if k>A[0][0]:
        return supprimer(A[2],k)
    
    if A[1]==[]:
        dropped,A[:]=A[0],A[2]
        return dropped
    if A[2]==[]:
        dropped,A[:]=A[0],A[1]
        return dropped
    m=supprime_min(A[2])
    A[:]=[m,A[1],A[2]]
    return A[0]


# In[8]:


A,_=initialiser()
print(A)


# In[9]:


supprimer(A,8)
print(A)


# La fonction de suppression a elle aussi un coût temporel en $O(h(A))$ puisque chaque appel récursif s’effectue sur un arbre de hauteur inférieur au précédent.

# ## Requêtes dans un arbre binaire de recherche

# ### Recherche d’une clé
# Une des opérations les plus courantes dans un arbre binaire de recherche $A$ = $[Fg;(c;v);Fd]$ est la recherche
# d’une valeur associée à une clé particulière $k$.
# <BR>La démarche est évidente :
# > - si $k = c$, retourner $v$ ;
# > - si $k < c$, rechercher $k$ dans $Fg$ ;
# > - si $k > c$, rechercher $k$ dans $Fd$.
# 
# Dans le cas où les clés ne sont pas toutes distinctes on retournera la valeur associée à la première clé égale à $k$ rencontrée.

# In[10]:


recherche=lambda A,k: None if A==[] else  A[0][1] if A[0][0]==k else recherche(A[1],k) if k<A[0][0] else recherche(A[2],k)


# In[11]:


recherche(A,12)


# ### 2.1 Recherche de la clé minimale / maximale
# La recherche de la valeur associée à la clé minimale se poursuit dans le fils gauche tant que ce dernier n’est pas
# vide :

# In[12]:


np.inf<10


# In[13]:


def recherche_min(A):
    if A==[]:
        #return (+infinie,"no min") si l'arbre est vide
        return (np.infty,"no min")
    #sinon poursivie la recherche dans le sous arbre gauche
    min_g=recherche_min(A[1])
    if A[0][0]<min_g[0]:
        return A[0]
    else:
        return min_g


# In[14]:


A,_=initialiser()
recherche_min(A)


# La fonction retournant la valeur associée à la clé maximale est symétrique :

# In[15]:


import numpy as np
type(np.infty)


# In[16]:


def recherche_max(A):
    if A==[]:
        #return (-infinie,"no max") si l'arbre est vide
        return (-np.infty,"no max")
    #sinon poursivie la recherche dans le sous arbre droit
    max_d=recherche_max(A[2])
    if A[0][0]>=max_d[0]:
        return A[0]
    else:
        return max_d


# In[17]:


recherche_max(A)


# ### Recherche du prédécesseur / successeur
# $k\in C$ étant donné, il s’agit cette fois de retourner la valeur associée à la plus grande des clés c contenues dans l’arbre et vérifiant :  $ c < k$ (respectivement $c > k$)

# In[18]:


def prédécesseur(A,k):
    if A==[]:
        return None
    if A[0][0]<k:
        pred=prédécesseur(A[2],k)
        return A[0][1] if pred == None else pred
    else:
        return prédécesseur(A[1],k)


# In[19]:


print("prédécesseur de: ")
for e in L:
    print("\t{} < {}".format(prédécesseur(A,e[0]),e[1]))


# In[20]:


def successeur(A,k):
    if A==[]:
        return None
    if A[0][0]>k:
        succ=successeur(A[1],k)
        return A[0][1] if succ is None else succ
    else:
        return successeur(A[2],k)


# In[21]:


print("prédécesseur | clé | successeur ")
for e in L:
    print("\t{} < {}<{}".format(prédécesseur(A,e[0]),e[1],successeur(A,e[0])))


# ### Complexité temporelle
# Toutes ces fonctions ont à l’évidence un coût temporel en $O(h(A))$, ce qui explique tout l’intérêt qu’il peut y avoir à ce que l’arbre binaire de recherche soit équilibré : dans un arbre binaire quelconque d’ordre $n = taille(A)$, on peut affirmer que le coût d’une requête est un $O(n)$ ; dans le cas d’un arbre de recherche équilibré, on peut assurer un coût en $O(log(n))$
