Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Estou aprendendo Python')
Estou aprendendo Python
>>> print ('Olá, Mundo!')
Olá, Mundo!
>>> print (7+4)
11
>>> print ('7'+'4')
74
>>> 7+4
11
>>> '7' + '4'
'74'
>>> nome='Guanabara'
>>> idade=25
>>> peso=75.8
>>> print('nome,idade,peso')
nome,idade,peso
>>> print(nome, idade, peso')
...       
SyntaxError: incomplete input
>>> print('nome, idade, peso')
...       
nome, idade, peso
>>> nome='Guanabara'
...       
>>> idade=25
...       
>>> peso=74.8
...       
>>> print('nome, idade, peso')
...       
nome, idade, peso
>>> nome = 'Guanabara'
...       
>>> peso = 74.8
...       
>>> idade = 25
...       
>>> print (nome, idade, peso)
...       
Guanabara 25 74.8
>>> print (nome+ idade+ peso)
...       
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print (nome+ idade+ peso)
TypeError: can only concatenate str (not "int") to str
>>> nome = input('Qual é seu nome?')
...       
Qual é seu nome?
>>> nome = input ('Qual é seu nome?')
...       
Qual é seu nome?Luis
>>> idade = input ('Qual a sua idade?')
...       
Qual a sua idade?24
>>> peso = input ('Qual o seu peso?')
...       
Qual o seu peso?89
>>> print (nome, idade, peso)
...       
Luis 24 89
