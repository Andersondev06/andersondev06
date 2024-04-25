#declarando variaveis
n1 = float(input('Quanto de largula tem a parede?: '))
n2 = float(input('Quantos metros tem a parede?: '))
r = n2*n1
l = r/605
a = l*(1/2)
print('Você vai precisar de {:.2f} litros de tinta para pintar essa parede'.format(l))

