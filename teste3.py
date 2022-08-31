numero_texto = 50
numero = int(numero_texto)
print('olá, vamos ao teste')
print('-----------------------')
print('Tenho um número guardado em minha memória, tente advinhar.')
chute = int(input('Para isso, digite um número:'))
print('............')
print('Você digitou o número:',chute,)
if (chute == numero):
    print('Show de bola, você acertou o número secreto')
elif (chute > numero):
    print('Poxa vida, o seu chute foi maior que o número gravado em minha memória')
elif (chute < numero):
    print('Poxa vida, o seu chute foi menor que o número gravado em minha memória')
print('Obrigado por participar!! Tchau!!')
