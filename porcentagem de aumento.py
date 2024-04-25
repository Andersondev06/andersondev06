#declarando variaveis
n1 = float(input('Digite o salario do colaborador:'))
n2 = float(input('Digite quantos % o salario ira aumentar: '))
r = (n1*n2)/100
b = r + n1 
print('O aumento foi de {}'.format(r))
print('O valor total do novo salario do colaborador é {}'.format(b))
