# Istruzione che stampa sulla schermo il messaggio 'Inserisci un numero intero: ',
# legge la sequenza di caratteri inserita e la salva nella variabile s
s = input('Inserisci un numero intero: ')
# Condizione che verifica che la stringa contenga un numero, eventualmente con segno
if s.isdecimal() or ((s[0] == '-' or s[0] == '+') and s[1:].isdecimal()):
    n = int(s) # Istruzione che trasforma la stringa s in numero e la salva nella variabile n
    x = n*n    # Istruzione che calcola il quadrato di n e lo salva nella variabile x
    print(x)   # Istruzione che stampa sullo schermo il valore di x
else:          # Se la condizione non è verificata allora stampa messaggio errore 
    print('Hai inserito un valore non numerico')
print('Finito') # Istruzione che viene eseguita comunque (fuori dal if else)
