#!/usr/bin/env python
# coding: utf-8

# # Teoría de Conjuntos

# La teoría de conjuntos es una rama de la lógica-matemática que se encarga del estudio de las relaciones entre entidades denominadas conjuntos. Los conjuntos se caracterizan por ser colecciones de objetos de una misma naturaleza. Dichos objetos son los elementos del conjunto y pueden ser: números, letras, figuras geométricas, palabras que representan objetos, los objetos mismos y otros.

# ## Creación de conjuntos
# 
# En python, puedes crear un conjunto utilizando llaves {} o la función set()

# In[1]:


A = {1, 2, 3, 4, 5}


# In[2]:


B = {3, 4, 5, 6, 7}


# In[3]:


c = set([3, 6, 9, 12, 15])


# In[ ]:





# ## Listas vs Conjuntos

# 

# In[4]:


lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


# In[5]:


lista


# In[6]:


conjunto = set(lista)


# In[7]:


conjunto


# ## Operaciones
# 
# Python proporciona operadores y métodos para realizar operaciones básicas de ocnjuntos ocmo unión, intersección, diferencia y diferencia simétrica.

# In[ ]:





# ## Unión

# La operación de unióhn en teoría de conjuntos es una operación que combina dos conjuntos para formar un nuevo conjunto que contiene todos los elementos que pertenecen a al menos uno de los conjuntos originales, sin duplicados. En otras palabras, la unión de dos conjuntos A y B, denotada como A B, contiene todos los elementos que están en A y B

# ![R.jpg](attachment:R.jpg)

# $$
#     C = A \cup B = {x:x \in A \quad o \quad x \in B}
# $$

# En python, la operación de unión puede realizarse utilizando el operador | o el método unión ()

# In[14]:


A | B


# In[16]:


A.union(B)


# In[ ]:





# ## Intersección

# Siempre que hablamos de la intersección entre dos conjuntos, significa un conjunto resultante que contiene todos los elementos comunes entre estos dos conjuntos. Alternativamente, también podemos decir que contiene todos los elementos de un conjunto que también pertenecen al otro conjunto. 

# ![OIP.jpg](attachment:OIP.jpg)

# $$
# A \cap B
# $$

# En python, la operación de intersección puede realizarse utilizando el operador & o el método intersección ()

# In[18]:


A & B


# In[17]:


A.intersection(B)


# In[ ]:





# ## Diferencia

# En teoría de conjuntos, la diferencia entre dos conjuntos es una operación que da como resultado otro conjunto con los elementos del primer conjunto sin los elementos del segundo conjunto

# 

# $$
#     \ A \setminus B \
# $$

# En python, la operación diferencia puede realizarse utilizando el operador - o el método diferencia()

# In[25]:


A - B


# In[26]:


B - A


# In[21]:


A.difference(B)


# In[27]:





# ## Diferencia simétrica

# La diferencia simétrica de dos conjuntos se puede definir como el conjunto de elementos que pertenecen a uno de los conjuntos iniciales, pero que no pertenecen a los dos. Por ejemplo, la diferencia simétrica de {4,2,3,8} y {1,2,3,7} es {1,4,8}.

# ![OIP%20%282%29.jpg](attachment:OIP%20%282%29.jpg)

# $$
# \ A \triangle B \
# $$

# En python, la operación diferencia simétrica puede realizarse utilizando el operador ^

# In[24]:


A ^ B


# In[ ]:





# ## Diagrama de Venn

# El diagrama de Venn es un tipo de organizador gráfico que muestra cómo se relacionan dos o más conjuntos de elementos, puesto que, mediante círculos superpuestos, representa qué características comparten y cuáles no dos o más categorías, grupos, ideas, conceptos, teorías, entre otros.

# ![OIP%20%283%29.jpg](attachment:OIP%20%283%29.jpg)

# In[31]:


pip install matplotlib_venn


# In[47]:


import matplotlib.pyplot as plt
import matplotlib_venn as venn


# A continuación un diagrama de Venn de 3 elementos:

# In[50]:


venn.venn2([A, B],set_labels = ("A", "B"))

