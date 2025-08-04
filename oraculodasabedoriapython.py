print('🔮 Bem-vindo ao Oráculo da Sabedoria Python!')
print('Pergunte-me sobre um tema de programação e eu te darei uma resposta sábia! 🤓')

assunto = input('Digite um tema (ex: variáveis, loops, funções, listas): ')

match assunto.lower():
    case 'variáveis':
        print('🧠 Variáveis são como caixinhas onde você guarda informações para usar depois!')
    case 'loops' | 'laços':
        print('🔁 Loops servem para repetir comandos até cansar... ou até uma condição ser falsa!')
    case 'funções':
        print('🔧 Funções são receitas de bolo: você chama, passa os ingredientes (parâmetros) e recebe o bolo pronto (retorno).')
    case 'listas':
        print('📋 Listas são coleções de itens, como uma fila de tarefas esperando para serem processadas.')
    case _:
        print('🤖 Ainda estou aprendendo sobre esse assunto... Pergunte-me novamente mais tarde!')
