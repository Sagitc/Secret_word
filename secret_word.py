import os

def clearTerminal():
    os.system('cls')

def checkQuit(valor):
    if valor == "sair" or valor == "quit" or valor == "exit":
        return True

def checkNeutral(valor):
    if valor == "" or valor == " ":
        return True

def checkPositiv(valor):

    valor =  valor.replace('.','').lower()

    if valor == "sim" or valor == "s" or valor == "yes" or valor == "y":
        return True
    else: 
        return False
    
def checkNegativ(valor):
    
    valor =  valor.replace('.','').lower()

    if valor == "não" or valor == "nao" or valor == "no" or valor == "n":
        return True
    else: 
        return False

def tips():
    dica1 = None
    dica2 = None

    print('\nVocê pode incluir até 2 dicas.\n' + 'Se não desejar incluir mais dicas, deixe em branco.')
    while dica1 != "" and dica2 != "" and dica1 != " " and dica2 != " ":

        dica1 = input('\nPrimeira dica: ')
        if checkQuit(dica1):
            quit()
        elif checkNeutral(dica1):
            user_answer = input(f'\nTem certeza que deseja sair sem adicionar nenhuma dica? ')
            if checkPositiv(user_answer):
                break
            elif checkNegativ(user_answer):
                dica1 = None
                continue
            else:
                print('\nResposta inválida.')
                input('Pressione <enter> para continuar.')
                continue
        elif checkPositiv(dica1) or checkNegativ(dica1):
            print('\nResposta inválida.')
            input('Pressione <enter> para continuar.')
            continue

        dica2 = input('Segunda dica: ')
        
        if checkNeutral(dica2):
            break
        elif checkQuit(dica2):
            quit() 

    print('\nAs dicas fornecidas serão exibidas durante o jogo')
    input('Pressione <enter> para continuar.')
    return dica1, dica2

tip1 = None
tip2 = None
user_word = ""
user_answer = ""
tentativas = 0

clearTerminal()

#####                                     #####
####                                      ####
#####           PARTE DO MESTRE           #####
####                                      ####
#####                                     #####
####                                      ####

print('PART 1 - MASTER')

while True:
    secret_word = input('\nInforme a palavra/frase secreta: ').lower()

    if checkQuit(secret_word) or checkNegativ(secret_word) or checkPositiv(secret_word) or checkNeutral(secret_word) or secret_word.isdigit():
        print('\nNão é possível definir essa palavra como a palavra secreta.')
        input('Pressione qualquer tecla para continuar')
        continue
    elif len(secret_word) < 3:
        print('A palavra/secreta deve contem no mínimo 3 letras.')
        continue
    elif len(secret_word) > 2:
        break

while True:
    user_answer = input('\nDeseja incluir uma dica? ').lower()
    if checkQuit(user_answer):
        quit()
    elif checkPositiv(user_answer):
        tip1, tip2 = tips()
        break
    elif checkNegativ(user_answer):
        break
    else:
        print('\nResposta inválida, tente novamente.')
        input('Pressione qualquer tecla para continuar')
        continue


for letter in secret_word:
    if letter == " ":
        user_word += " "
    else:
        user_word += '*'

secret_list =  list(user_word)

clearTerminal()


###                                               ###   
##                                                ## 
###                 PARTE DO PLAYER               ###
##                                                ##
###                                               ###


print('PART 2 - PLAYER')

while True:
    guess_word = ''.join(secret_list)

    if tentativas == (len(secret_word)//2) and tip1 != 'sair' and tip1 != '' and tip1 != ' ' and tip1 != None:
        print('\nAqui vai uma dica para você: ',tip1)
        input('\nPressione qualquer tecla para continuar')
        clearTerminal()
        print('PART 2 - PLAYER')
    if tentativas == len(secret_word) and tip2 != 'sair' and tip2 != '' and tip2 != ' ' and tip2 != None:
        print('\nDifícil? Última dica: ',tip2)
        input('\nPressione qualquer tecla para continuar')
        clearTerminal()
        print('PART 2 - PLAYER')

    if tentativas%5 == 0 and tentativas != 0:
        print('\nGrande chance de advinhar a palavra/frase completa')
        print('\n'+guess_word)
        user_answer = input('Qual é o seu palpite? ')

        if checkQuit(user_answer):
            quit()
        elif checkNegativ(user_answer) or checkPositiv(user_answer) or checkNeutral(user_answer):
            print('\n Resposta inválida.')
            input('Pressione qualquer tecla para continuar')
            tentativas += 1
            continue
        elif user_answer == secret_word:
            tentativas += 1
            break
        else:
            print('\nResposta incorreta.')
            input('Pressione qualquer tecla para continuar')
            tentativas += 1
            continue

    user_letter = input('\nDigite uma letra: ').lower()

    if checkQuit(user_letter):
        quit()
    elif len(user_letter) > 1 or len(user_letter) <= 0 or user_letter.isdigit():
        print('Digite apenas uma letra.')
        continue

    if user_letter in secret_word:
        contador = 0
        for i in secret_word:
            if i == user_letter:
                secret_list[contador] = i
                contador += 1
            else:
                contador += 1
                continue
        guess_word = ''.join(secret_list)
        print('Progresso: '+guess_word)
    else:
        print('Progresso: ' + guess_word)
        tentativas += 1
        continue

    if guess_word == secret_word:
        tentativas += 1
        break

    tentativas += 1

print(f'\nParabéns, você conseguiu em {tentativas} tentativas!')
print(f'A palavra secreta era "{secret_word}"\n')
input('Pressione qualquer tecla para coninuar.')
quit()