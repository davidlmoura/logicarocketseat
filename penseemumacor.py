import os
import sys
import random
sys.stdout.reconfigure(encoding='utf-8')

os.system('cls')

print('🎨✨ Prepare-se para um truque de mágica incrível!')
print('Pense em uma cor... qualquer cor! Mas não me diga qual é! 🤫')
print('Quando estiver pronto, aperte ENTER para continuar.')
input()

print('🔮 Estou me concentrando...')
input('Aperte ENTER quando estiver pronto para a revelação!')

cores_possiveis = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo', 'laranja', 'preto', 'branco']
cor_adivinhada = random.choice(cores_possiveis)

print(f'🌈 {cor_adivinhada.upper()}!!! 🎉✨')
print('Aposto que você ficou surpreso agora, hein? 😏🧙‍♂️')
