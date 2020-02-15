
# coding: utf-8

# ### Ricapitolazione Lez 3
# - operatore in
# - while: condizione iniziale, ordine delle istruzioni, cicli infiniti
# - attenzione all'and 
# - scansione di una stringa con il while o con il for
# - for: i in elenco, indicizza su un elenco di oggetti, non tipato
# - for se elementi di una stringa vs for su indici di una stringa
# - funzione range
# - disegni con asterischi

# # Lez 4
# 
# ## Definizione di funzioni
def<nome funzione> (<parametri formali>):
    blocco di istruzioni
    return<valore>
# In[11]:

def raddoppia (n):
    n=n*2
    return n


# In[12]:

raddoppia (5)


# In Java ed in C dovete dichiarare in anticipo il tipo dentro la funzione! Questo permette un controllo più forte, è più robusto, ho un controllo maggiore su quello che succede!
# In python no, potente ma anche pericoloso! Python non prevede il controllo di tipi!

# In[13]:

raddoppia('cavolo')


# In[14]:

raddoppia([0,1])


# In[15]:

raddoppia(raddoppia(3))


# In[59]:

def raddoppia (n):             # n è il parametro FORMALE  
    n=n*2
    return n

raddoppia(4)                # 4 è il parametro ATTUALE


# OSS: Ricordatevi che vedete il risultato di raddoppia (6) solo dentro la shell, se scrivete sull'editor la funzione radoppia(6) senza assegnarla a nessuna variabile, l'istruzione non viene visualizzata ed è completamente persa!State attenti! La shell va usata per capire, è comodo vedere il risultato subito!!! Non programmate tutto dentro la shell!

# In[16]:

def raddoppia (n):             
    n=n*2
    k=5
    print(n)
    return n  

raddoppia(4)


# In[17]:

k


# ### Funzioni con più parametri 

# In[18]:

def prodotto(n,m):
    p=n*m
    return p


# In[19]:

# tab vede anche la nostra funzione ora
prodotto(3,2)


# I parametri della chiamata (i parametri attuali) devono corrispondere come numero a quelli formali a meno che io non abbia dato un valore di default ai miei parametri. 
# (In altri linguaggi anche il tipo deve essere lo stesso)

# ### Funzioni con parametri inizializzati

# In[99]:

def potenza(n,m=1):      # se io nella chiamata non do un valore al secondo param lui prende
    p=n**m                 # quello di default
    return p


# Anche questo è difficile da fare con altri linguaggi di programmazione!

# In[101]:

potenza(2)


# !!!! I default devono sempre essere in fondo alla lista !!!!

# In[20]:

help(print)


# In[110]:

potenza(2,m=3)


# In[113]:

potenza(m=3,n=2)

Lavorare per funzioni permette di separare i problemi!!!
# Esempio: i controlli che un numero in input sia un intero dentro il codice appesantice il codice, faccio il controllo in modo differente. La soluzione è scrivere una funzione una volta per tutte che controlla che il numero è intero!!!
Le funzioni ci permettono di concentrare istruzioni complesse in un blocco di codice con un nome di vostra fantasiaUn funzione può richiamare un'altra funzione!!!!!!! Una funzione può avere o no input, output ed effetti collaterali !!!!!
# ### Sviluppo incrementale:
# - Inizia con un programma funzionante e fai piccoli cambiamenti
# - Usa variabili temporanee per memorizzare i valori intermedi, per stamparli e controllarli
# - Alla fine rimuovi le istruzioni temporanee e componi le istruzioni se non complica troppo il programma

# ## Liste
# 
# Comodissime, potentissime!!! Non ha equivalenti con altri linguaggi di programmazione per come è fatta in python. La lista è un insieme di elementi eterogenei e mutabili!!!

# In[21]:

l=['ciao',19,3.1]

!!!! Le liste possono essere cambiate le stringhe no!!!!!!!!! Attenzione !!!! se assegno ad un'altra variabile l, eg. lbis=l non sto creando un nuovo elemento come nelle stringhe, è sempre lo stesso elemento, le tue variabili puntano alla stessa lista!!!!
# In[23]:

lbis=l
l[0]='domani'
l


# In[24]:

lbis

Le variabili sono puntatori all'oggetto di riferimento!!!!
# In[25]:

# per aggiungere elementi ad una lista
l.append(3)


# In[27]:

lbis


# In[28]:

### !!!! il comando qui sotto non modifica la lista ma ne crea una nuova ###
l = l+['ciao']

##### Ora lbis ed l puntatno a due cose diverse


# In[29]:

l


# In[30]:

lbis


# In[32]:

s='oggi è una bella giornata'
s.split()


# In[160]:

help(s.split)


# ### Esercizio: 
# fare una funzione che prende in input una lista di interi e li ordina usando un insettionsort algorithm

# In[ ]:



