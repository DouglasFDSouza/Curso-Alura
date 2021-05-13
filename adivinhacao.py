def jogo_adivinhacao():

    import random

    print('***************************************') 
    print('Bem Vindo ao nosso jogo de Adivinhação!')
    print('***************************************')

    numero_secreto = random.randint(1,100)
    pontos = 1000

    print('Fácil[0] Médio[1] Difícil[2]')
    dificuldade = int(input('Selecione a dificuldade: '))
    if(dificuldade == 0):
        tentativas = 20
    elif (dificuldade == 1):
        tentativas = 10
    elif (dificuldade == 2):
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print('Rodada {} de {}'.format(rodada, tentativas))
        chute = int(input('Digite um número entre 1 e 100: '))
        print('O número escolhido foi', chute)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100')
            continue
        if (chute == numero_secreto):
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if (chute > numero_secreto):
                print('O seu número foi maior que o número escolhido')
            elif (chute < numero_secreto):
                print('O seu número foi menor que o número escolhido')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('Fim de jogo!')

if (__name__ == '___main__'):
    jogo_adivinhacao()