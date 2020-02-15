'''
#  verifico che la stringa contenga un numero con o senza segno
convertibile=False
while not convertibile:
    print("Il numero inserito non e' un numero intero" )
    s=input("Inserisci un numero intero: ")
    convertibile = len(s)>0 and (s.isdecimal() or                         #mettendo le parentesi 
                    ((s[0] in '+-') and s[1:].isdecimal()))    #posso andare a capo   
n=int(s)
print("Intero inserito =",n )
'''


#  verifico che la stringa contenga un numero con o senza segno,
#  con lettura prima del ciclo
s=input("Inserisci un numero intero: ").strip()
convertibile=len(s)>0 and (s.isdecimal() or 
                    ((s[0] in '+-') and s[1:].isdecimal()))
while not convertibile:
    print("Il numero inserito non e' un numero intero")
    s=input("Inserisci un numero intero: ").strip()
    convertibile = len(s)>0 and (s.isdecimal() or                         
                    ((s[0] in '+-') and s[1:].isdecimal()))    
n=int(s)
print("Intero inserito =",n )

