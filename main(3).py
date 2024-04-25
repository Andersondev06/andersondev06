#declarando variaveis
n = (input('Digite algo : '))
print(type(n))
print('1- é um numero? ',n.isnumeric())
#se o é numero ou não
print('2- é alfabeto? ',n.isalpha())
#se é texto ou não
print('3- é um alfanumerico? ',n.isalnum())
#se é numero e letra juntos
print('4- está em maisculo? ',n.isupper())
#se existe letra maiuscula
print('5- Só tem espaço? ',n.isspace())
#se só existe espaço
print('6- está em maisculo? ',n.islower())
#se esta em minusculo
print('7- esta capitalizada?',n.istitle())
#se esta escrito com maisculo e minusculo

