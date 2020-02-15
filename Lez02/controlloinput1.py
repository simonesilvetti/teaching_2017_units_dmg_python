#programma che controlla ingresso input
s=input("Inserisci un numero intero: ")

#  verifico che la stringa contenga un numero con o senza segno
if s.isdecimal():
    n=int(s)
    print("Intero inserito=",n )
else:
    print("Il valore inserito non è un intero")
