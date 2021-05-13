import random


print('***********************')
print('Bem-vindo ao jogo forca')
print('***********************')

#carrega a palvra secreta
arquivo = open('palavras.txt')
palavras = []
for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)
arquivo.close()
numero = random.randrange(0, len(palavras))
palavra_secreta = palavras[numero]
letras_acertadas = ['_' for letra in palavra_secreta]


enforcou = False
acertou = False
erros = 7

print(letras_acertadas)

while(not enforcou and not acertou):

    chute = input('Qual letra?').strip().lower()

    if(chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas [index] = letra
            index += 1
    else:
        erros -= 1
        print('Restam {} tentativas'.format(erros-1))
        

    enforcou = erros == 0
    acertou = '_' not in letras_acertadas 
    print(letras_acertadas)
    

if (acertou):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
else:
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
print('Fim do jogo')


