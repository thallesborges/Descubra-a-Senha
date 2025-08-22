import random, time

while True:
    senha = str(random.randint(123, 9999)).zfill(4)
    digitos_senha = list(senha)

    if len(digitos_senha) == len(set(digitos_senha)):
        break

tentativa = 1
digitos_errados = set()
palpites_feitos = []

while tentativa <= 5:
    print(f'== Tentativa ({tentativa}/5) ==')

    while True:
            palpite = input('Senha: ')
            if len(palpite) != 4:
                print('!! Por favor, insira uma senha númerica de 4 dígitos.')
                continue
            try:  
                digitos_palpite = list(palpite)
                break
            except ValueError:
                print('!! Por favor, insira uma senha numérica de 4 dígitos.')
    
    palpites_feitos.append(palpite)
    digitos_certos_posicao_correta = 0
    digitos_certos_posicao_errada = 0

    for i in range(4):
        if digitos_palpite[i] == digitos_senha[i]:
            digitos_certos_posicao_correta += 1

    palpite_restante = []
    senha_restante = []

    if digitos_certos_posicao_correta == 4:
        time.sleep(2)
        print('== Parabéns, você descobriu a senha! Cofre aberto com sucesso 🎉')
        break

    for i in range(4):
        if digitos_palpite[i] != digitos_senha[i]:
            palpite_restante.append(digitos_palpite[i])
            senha_restante.append(digitos_senha[i])
    
    for digito in palpite_restante:
        if digito in senha_restante:
            digitos_certos_posicao_errada += 1
            senha_restante.remove(digito)
        else:
            digitos_errados.add(digito)

    time.sleep(1)
    print(f'Existem {digitos_certos_posicao_correta} dígito(s) correto(s) e na posição CORRETA.')
    print(f'Existem {digitos_certos_posicao_errada} dígito(s) correto(s), mas na posição ERRADA. ')
    print(f'== Dígitos errados: {', '.join(str(digito) for digito in sorted(digitos_errados))}')
    print(f'== Palpites feitos anteriormente: {', '.join(f'{i}. {palpite}' for i, palpite in enumerate(palpites_feitos, start=1))}')
    time.sleep(2)
    tentativa += 1

else:
    print('== Tentativas esgotadas. Cofre bloqueado! 🔐')
    print(f'A senha era: {senha}')