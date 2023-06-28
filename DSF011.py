# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
a = float(input('Qual a altura da sua parede?: '))
l = float(input('Qual a largura da sua parede?: '))
t = (a * l) / 2
print('A quantidade de tinta necessária é de {} litros'.format(t))
