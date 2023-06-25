#!/usr/bin/env python
# coding: utf-8

# # Arbres binaires

# ### Définition formelle d’un arbre binaire

# On appelle arité d’un nœud le nombre de branches qui en partent 3 . Dans la suite de notre cours, nous nous intéresserons plus particulièrement aux arbres binaires, c’est à dire ceux dont chaque nœud a au plus deux fils.</br>
# Pour ne pas avoir à distinguer les nœuds suivant leur arité, il est pratique d’ajouter à l’ensemble des arbres binaires un arbre particulier appelé l’arbre vide. Ceci conduit à adopter la définition qui suit.

# <div class="alert alert-success" >
#      Un ensemble E étant donné, on définit par induction les arbres binaires étiquetés par E en convenant que :
# <ul>
# <li> [  ] : est un arbre binaire sur E appelé l’arbre vide ;
# <li> si x ∈ E et si Fg et Fd sont deux arbres binaires étiquetés par E, alors A = [x,Fg , Fd ] est un arbre binaire étiqueté par E.
# </ul>
# </div>

# x est l’étiquette de la racine de A ; quant à Fg et Fd , ils sont appelés respectivement le sous-arbre gauche et le sous-arbre droit de l’arbre binaire A.<br>
# De manière usuelle, on convient de ne pas faire figurer l’arbre vide dans les représentations graphiques des arbres binaires. Ainsi, suivant la représentation choisie les feuilles pourront désigner exclusivement l’arbre vide (et dans ce cas tous les nœuds seront d’arité égale à 2) ou alors les nœuds dont les deux fils sont vides (dans ce cas l’arité d’un nœud pourra être égale à 0, 1 ou 2). C’est cette seconde convention qui sera utilisée dans la suite de ce cours.

# **Définition.**<br> La **taille(A)** d’un arbre A est définie inductivement par les relations :
# > taille([  ]) = 0 ;<br>
# > Si A = (Fg , x, Fd ) alors taille(A)= 1 + taille(Fg) + taille(Fd).

# **Définition.**<br> **La hauteur**: h(A) d’un arbre A se définit inductivement par les relations :
# > h([ ]) = 0 ;<br>
# > Si A = (Fg , x, Fd ) alors h(A) = 1 + max(h(Fg ), h(Fd )).

# Avec ces conventions, taille(A) est le nombre de nœuds d’un arbre et h(A) la longueur maximale du chemin reliant la racine à une feuille, autrement dit la profondeur maximale d’un nœud.<br>
# La définition Python de ces fonctions est immédiate :

# In[1]:


Vide=[]
f1=[1,Vide,Vide]
f0=[0,[],[]]


# In[2]:


f2=[1,f1,f0]


# In[3]:


f2


# In[4]:


def FiboA(n):
    if n<=1:
        return [n,[],[]]
    Fg=FiboA(n-1)
    Fd=FiboA(n-2)
    racine=Fg[0]+Fd[0]
    return [racine,Fg,Fd]


# ![fibtree5.png](fibtree5.png)

# In[5]:


F4=FiboA(4)


# In[6]:


def taille(A):
    if A==[]:
        return 0
    return 1+taille(A[1])+taille(A[2])


# In[7]:


def hauteur(A):
    if A==[]:
        return 0
    return 1+max(hauteur(A[1]),hauteur(A[2]))


# In[8]:


hauteur(F4)


# In[9]:


def parcour_prefixe(A):
    if A==[]:
        return []
    return [A[0]]+parcour_prefixe(A[1])+parcour_prefixe(A[2])


# In[10]:


def parcour_postfixe(A):
    if A==[]:
        return []
    return parcour_postfixe(A[1])+parcour_postfixe(A[2])+[A[0]]


# In[11]:


parcour_prefixe(F4)


# In[12]:


def parcour_infixe(A):
    if A==[]:
        return []
    return parcour_infixe(A[1])+[A[0]]+parcour_infixe(A[2])


# In[13]:


print("prefixe: ",parcour_prefixe(F4))
print("postfixe: ",parcour_postfixe(F4))
print("infixe: ",parcour_infixe(F4))


# In[14]:


def parcour_en_largeur(A):
    L1,L2=[A],[]
    larg=[]
    while L1!=[]:
        for E in L1:
            if E!=[]:
                larg.append(E[0])
                L2.extend([E[1],E[2]])
        L1=L2
        L2=[]
    return larg


# In[15]:


parcour_en_largeur(FiboA(4))


# In[16]:


print("La taille de F(4) est {}, et son hauteur est {}".format(taille(F4),hauteur(F4)))

