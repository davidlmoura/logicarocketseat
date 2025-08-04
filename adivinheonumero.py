import random
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

os.system('cls')

print('🎩✨ Bem-vindo ao meu incrível truque de mágica!')
print('Pense em um número de 1 a 10... Não me diga qual é! 🤐')
print('Quando estiver pronto, aperte ENTER para continuar.')
input()

print('🔮 Estou lendo sua mente...')
input('Hmmmm... Estou quase lá... (pressione ENTER)')

numero = random.randint(1, 10)

print()
print('Eu sei qual número você pensou! 😱✨')
print(f'Você pensou no número... {numero}!!! 🧙‍♂️🎉')
print('Isso foi mágico ou apenas sorte? Nunca saberemos... 😏')
