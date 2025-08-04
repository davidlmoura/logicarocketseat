print('🔐 Jogo do Número Secreto! Tente adivinhar o número escondido! 🎲')
print('Dica: o número está entre 1 e 10!')

numero_secreto = 7  # Número fixo escolhido
tentativas = 0
acertou = False

while not acertou:
    chute = input('Digite seu palpite: ')
    
    if chute.isdigit():
        chute = int(chute)
        tentativas += 1
        if chute == numero_secreto:
            print(f'🎉 Parabéns! Você acertou o número secreto {numero_secreto}!')
            print(f'Você precisou de {tentativas} tentativa(s) para acertar! 👏')
            acertou = True
        else:
            print('❌ Ainda não é esse número... tente novamente!')
    else:
        print('Por favor, digite apenas números inteiros.')
