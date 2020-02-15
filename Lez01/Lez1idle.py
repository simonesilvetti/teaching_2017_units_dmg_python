>>> 
======== RESTART: C:/Users/dmg-nenzi/Documents/Python Scripts/ciao.py ========
3
6
>>> print(3)
3
>>> print(3+3)
6
>>> print('3')
3
>>> print("3")
3
>>> print('ciao')
ciao
>>> print("'ciao'")
'ciao'
>>> 'ciao'
'ciao'
>>> 3+3
6
>>> 
======== RESTART: C:/Users/dmg-nenzi/Documents/Python Scripts/ciao.py ========
>>> print('3'+'3')
33
>>> print('3'+' 3')
3 3
>>> print(3,'+',3)
3 + 3
>>> 2*4
8
>>> 2**4
16
>>> 2**1024
179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137216
>>> 2.0**1024
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    2.0**1024
OverflowError: (34, 'Result too large')
>>> print('ciao'*5)
ciaociaociaociaociao
>>>  print(3)
 
SyntaxError: unexpected indent
>>> x = 5
>>> x = 5+5
>>> type(x)
<class 'int'>
>>> s ='ciao'
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'ciao'
>>> c='3'
>>> int(c)
3
>>> 
======== RESTART: C:/Users/dmg-nenzi/Documents/Python Scripts/ciao.py ========
>>> z
5
>>> c
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> s='ciao'
>>> x=3
>>> y=str(3)
>>> s[0]
'c'
>>> s[3]
'o'
>>> len(s)
4
>>> z='hfhfhhffhfhsdeuociuheb c3784o6 0'
>>> z[len(z)-1]
'0'
>>> z[-1]
'0'
>>> input('Inserisci un numero: ')
Inserisci un numero: 5
'5'
>>> 
======== RESTART: C:/Users/dmg-nenzi/Documents/Python Scripts/ciao.py ========
inserisci un numero: 5
>>> 
======== RESTART: C:/Users/dmg-nenzi/Documents/Python Scripts/ciao.py ========
inserisci un numero: 5
>>> x
'5'
>>> type(x)
<class 'str'>
>>> 
======== RESTART: C:/Users/dmg-nenzi/Documents/Python Scripts/ciao.py ========
inserisci un numero: 55
>>> x
55
>>> str(x)
'55'
>>> 
======== RESTART: C:/Users/dmg-nenzi/Documents/Python Scripts/ciao.py ========
inserisci un numero: 55
>>> type(x)
<class 'int'>
>>> 
======== RESTART: C:/Users/dmg-nenzi/Documents/Python Scripts/ciao.py ========
inserisci un numero: ffff
Traceback (most recent call last):
  File "C:/Users/dmg-nenzi/Documents/Python Scripts/ciao.py", line 4, in <module>
    x = int(input('inserisci un numero: '))
ValueError: invalid literal for int() with base 10: 'ffff'

#### quando si salva un file della idle poi non può più essere usato come idle.
