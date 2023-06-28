#Crie um algoritmo que leia um número e mostre
# o seu dobro, seu triplo e raiz quadrada.
n1 = float(input('Digite um número: '))
d = float(2 * n1)
t = float(3 * n1)
r = float(n1 ** (1/2))
print('O dobro deste número é {}, o triplo é {} \n e sua raiz quadrada é {:.3f}'.format(d, t, r))
#{:.3f} >>> essa expressão limita 3 caracteres após virgula do resultado da conta onde
# .xf onde x delimita o número de pontos flutuantes, neste caso, 3 pontos flutuantes.
