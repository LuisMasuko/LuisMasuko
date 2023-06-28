# Faça um algoritmo que leia o preço de um produto e mostre seu
# novo preço, com 5% de desconto.
n = float(input('Qual o valor do produto? '))
d = n - (n * 0.05)
print('O valor do produto com desconto é {}'.format(d))
