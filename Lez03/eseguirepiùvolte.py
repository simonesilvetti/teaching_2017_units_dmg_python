finito = False
while not finito:
    exec(open('controlinput_while.py').read())
    finito =input('Finisco? ').lower()=='sì'
