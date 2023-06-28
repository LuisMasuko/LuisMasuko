# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros
n1 = float(input('Qual a medida em metros?: '))
c = n1 * 100
mm = n1 * 1000
print('A medida em metros é equivalente à {} centímetros e a {} milímetros'.format(c, mm))
