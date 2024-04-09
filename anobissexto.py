# condicionais / anobissexto.py
'''
Criar uma aplicação python, para identificar se um ano é bissexto.

Vai solicitar para o usuario informar o ano Retorna se o ano é bissexto ou não.

para ser bissexto tem que ser:

 MULTIPLO DE 4

3 NAO PODE SER DIVISIVEL POR 100 A NAO QUE SEJA POR 400.
'''
ano = int(input('digite o ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('o ano é bissexto')
else: 
    print('o ano não é bissexto')