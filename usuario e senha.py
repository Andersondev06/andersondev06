
# autenticação com usuario e senha
# declarando as viriaveis
login = input('digite seu usuario: ')
senha = input('digite sua senha: ')
#condições
if login == 'anderson'and senha == '123' or login == 'giovanna' and senha == '123':
   print('login ok')
   chave = input('digite a chave de segurança: ')
   if chave == 'abc'or chave == 'def':
       print('chave ok')
   else:
       print('chave invalida')
else:
   print ('login invalido')
   

    

