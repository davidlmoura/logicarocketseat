def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' | '.join(linha))
        print('-' * 11)

print('🚀 Bem-vindo à Caça ao Tesouro Espacial! 💎🪐')
print('O tesouro está escondido em um planeta misterioso... Tente encontrar!')

# Criando o tabuleiro 3x3
tabuleiro = [
    [' ' for _ in range(3)],
    [' ' for _ in range(3)],
    [' ' for _ in range(3)]
]

# Tesouro escondido na linha 1, coluna 2
tesouro_linha = 1
tesouro_coluna = 2

tentativas = 5

for tentativa in range(1, tentativas + 1):
    print(f'\nTentativa {tentativa} de {tentativas}')
    exibir_tabuleiro(tabuleiro)

    try:
        linha = int(input('Escolha a linha (0, 1 ou 2): '))
        coluna = int(input('Escolha a coluna (0, 1 ou 2): '))

        if not (0 <= linha <= 2 and 0 <= coluna <= 2):
            print('🚫 Posição inválida! Digite valores entre 0 e 2.')
            continue

        if tabuleiro[linha][coluna] != ' ':
            print('⚠️ Você já tentou essa posição! Escolha outra.')
            continue

        if linha == tesouro_linha and coluna == tesouro_coluna:
            tabuleiro[linha][coluna] = '💎'
            exibir_tabuleiro(tabuleiro)
            print('🎉 Parabéns! Você encontrou o tesouro espacial! 🚀💎')
            break
        else:
            tabuleiro[linha][coluna] = 'X'
            print('❌ Nada aqui... continue procurando!')

    except ValueError:
        print('Por favor, digite apenas números inteiros.')

else:
    print('\n💥 Suas tentativas acabaram! O tesouro estava em:')
    tabuleiro[tesouro_linha][tesouro_coluna] = '💎'
    exibir_tabuleiro(tabuleiro)
    print('Boa sorte na próxima aventura! 😉')

