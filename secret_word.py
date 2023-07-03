import getpass, os, sys

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def clearTerminal():
    os.system('cls')

clearTerminal()
print('Bem-vinda ao jogo da palavra ou frase secreta.\n')

secret_word = getpass.getpass('\nDigite a palavra secreta: ').lower()

user_answer = input('\nDeseja incluir uma dica? ').lower()

dica1 = None
dica2 = None

if user_answer == "sim" or user_answer == "s" or user_answer == "yes" or user_answer == "y":
    print('\nVocê pode incluir até 2 dicas.\n' + 'Se não deseja incluir mais dicas, digite "sair"')
    while dica1 != "sair" and dica2 != "sair" and dica1 != "" and dica2 != "":
        dica1 = input('\nPrimeira dica: ')
        if dica1 == "sair" or dica1 == "":
            continue
        dica2 = input('Segunda dica: ')
        if dica2 == 'sair' or dica2 == "":
            continue
    else:
        print('\nAs dicas fornecidas serão exibidas durante o jogo')
        input('Pressione "Enter" para continuar.')

user_word = ""
tentativas = 0

for letter in secret_word:
    if letter == " ":
        user_word += " "
    else:
        user_word += '*'

listletter =  list(user_word)

os.system('cls')

while True:

    if tentativas == 5 and dica1 != 'sair' and dica1 != '':
        print('\nAqui vai uma dica para você: ',dica1)

    guess_word = ''.join(listletter)
    user_letter = input('\nDigite uma letra: ').lower()

    if len(user_letter) > 1 or len(user_letter) <= 0 or user_letter.isdigit():
        print('Digite apenas uma letra.')
        continue

    if user_letter in secret_word:
        contador = 0
        for i in secret_word:
            if i == user_letter:
                listletter[contador] = i
                contador += 1
            else:
                contador += 1
                continue
        guess_word = ''.join(listletter)
        print('Progresso: '+guess_word)
    else:
        print('Progresso: ' + guess_word)
        tentativas += 1
        continue

    if guess_word == secret_word:
        break

    tentativas += 1

print(f'\nParabéns, você conseguiu em {tentativas} tentativas!')
print(f'A palavra secreta era "{secret_word}"\n')
user_answer = input('Deseja mais uma rodada? Sim ou não. ').lower()
if user_answer == "sim":
    restart_program()
else:
    quit()