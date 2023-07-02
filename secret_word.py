print('Bem-vinda ao jogo da palavra ou frase secreta.\n' + 'Uma letra por tentativa.\n')
print('Uma dica: Vimos o filme esses dia.\n')

user_word = ""
secret_word = 'wall e'
tentativas = 0

for letter in secret_word:
    if letter == " ":
        user_word += " "
    else:
        user_word += '*'

listletter =  list(user_word)

while True:

    if tentativas > 5:
        print('\nOutra dica: Evaaaa\n')

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

print(f'\nParabéns, você conseguiu em {tentativas} tentativas\n')