print('🎮 Bem-vindo ao Quiz de Perguntas e Respostas Python! 🧠✨')
print('Responda e veja quantos pontos você consegue fazer! Vamos lá! 🚀')
print()

perguntas = [
    ['Qual linguagem estamos usando neste quiz?', 'python'],
    ['Qual comando usamos para exibir algo na tela?', 'print'],
    ['Como chamamos um bloco de código reutilizável?', 'função'],
    ['Qual é o símbolo usado para comentários?', '#'],
    ['Qual estrutura usamos para repetir algo?', 'loop']
]

acertos = 0

for pergunta in perguntas:
    resposta = input(f'{pergunta[0]} ').lower()
    if resposta == pergunta[1]:
        print('✅ Acertou!')
        acertos += 1
    else:
        print(f'❌ Errou! A resposta certa era: {pergunta[1]}')
    print()

print(f'🏆 Você acertou {acertos} de {len(perguntas)} perguntas!')
if acertos == len(perguntas):
    print('PERFEITO! Você é um(a) verdadeiro(a) mestre Python! 🐍👑')
else:
    print('Continue praticando e logo você será um(a) mestre Python! 💪🐍')
