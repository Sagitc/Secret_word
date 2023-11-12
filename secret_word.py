import os

def clearTerminal():
    os.system('cls')

def checkPositiv(valor):

    word =  valor.replace('.','')

    if word == "sim" or word == "s" or word == "yes" or word == "y":
        return True
    else: 
        return False
    
def checkNegativ(valor):
    
    word =  valor.replace('.','')

    if word == "não" or word == "nao" or word == "no" or word == "n":
        return True
    else: 
        return False

def tips():
    dica1 = None
    dica2 = None

    print('\nVocê pode incluir até 2 dicas.\n' + 'Se não desejar incluir mais dicas, deixe em branco.')
    while dica1 != "sair" and dica2 != "sair" and dica1 != "" and dica2 != "" and dica1 != " " and dica2 != " ":
        dica1 = input('\nPrimeira dica: ')
        if dica1 == "sair" or dica1 == "exit":
            quit()
        elif dica1 == "" or dica1 == " ":
            continue
        dica2 = input('Segunda dica: ')
        if dica2 == 'sair' or dica2 == "exit":
            quit()
        elif  dica2 == "" or dica2 == " ":
            continue
        print('\nAs dicas fornecidas serão exibidas durante o jogo')
        input('Pressione <enter> para continuar.')
        break
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
    if secret_word == "sair" or secret_word == "exit":
        quit()
    elif len(secret_word) < 3:
        print('A palavra/secreta deve contem no mínimo 3 letras.')
        continue
    elif len(secret_word) > 2:
        break

while True:
    user_answer = input('\nDeseja incluir uma dica? ').lower()
    if user_answer == "sair" or user_answer == "exit":
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

    if tentativas == (len(secret_word)//2):
        user_answer = input('\nDeseja advinhar a palavra completar? ')

        if checkNegativ(user_answer):
            continue
        elif checkPositiv(user_answer):
            user_answer = input('\nQual é a palavra? ')
            if user_answer == secret_word:
                tentativas += 1
                break
            else:
                print('\nResposta incorreta.')
                input('Pressione qualquer tecla para continuar')
                tentativas += 1
                continue
        else:
            print('\nReposta inválida, tente novamente.')
            input('Pressione qualquer tecla para continuar')
            continue

    user_letter = input('\nDigite uma letra: ').lower()

    if user_letter == "sair" or user_letter == "exit":
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