#declarando variaveis
n1 = float(input('Digite o preço do produto: '))
n2 = float(input('Digite quantos % de desconto você quer: '))
r = (n1*n2)/100 
b = (n1 - r)
print('O desconto do produto é  {}'.format(r))
print('O valor total será {}'.format(b))
