# ✅ 1. Uma senha de 4 dígitos é gerada aleatóriamente
# ✅ 2. A senha correta deve ser informada pelo usuário
# ✅ 3. O usuário tem 5 tentativas para acertar a senha
# ✅ 4. A cada tentativa o sistema deve informar:
# --- Quantos dígitos estão corretos e na posição correta.
# --- Quantos dígitos estão corretos, mas na posição errada.
# ✅ 5. Se o usuário acertar, o sistema exibe: "Cofre aberto com sucesso!"
# ✅ 6. Se acabar as tentativas, exibe: "Tentativas esgotadas. Cofre bloqueado!"

import random

senha = str(random.randint(0, 9999))
digitos_senha = []

for i in senha:
    digitos_senha.append(int(i))

tentativa = 1
while tentativa <= 5:
    print(f'== Tentativa ({tentativa}/5) ==')

    while True:
            palpite = input('Senha: ')

            if len(palpite) != 4:
                print('!! Por favor, insira uma senha númerica de 4 dígitos.')
                continue
            
            try:  
                digitos_palpite = [int(digito) for digito in palpite]
                break
            except ValueError:
                print('!! Por favor, insira uma senha numérica de 4 dígitos.')

    digitos_certos_posicao_correta = 0
    digitos_certos_posicao_errada = 0

    for i in range(4):
        if digitos_palpite[i] == digitos_senha[i]:
            digitos_certos_posicao_correta += 1

    palpite_restante = []
    senha_restante = []

    for i in range(4):
        if digitos_palpite[i] != digitos_senha[i]:
            palpite_restante.append(digitos_palpite[i])
            senha_restante.append(digitos_senha[i])
    
    for digito in palpite_restante:
        if digito in senha_restante:
            digitos_certos_posicao_errada += 1
            senha_restante.remove(digito)

    if digitos_certos_posicao_correta == 4:
        print('Cofre aberto com sucesso!')
        break
    
    elif tentativa == 6:
        print('Tentativas esgotadas. Cofre bloqueado!')
        break
    
    else:
        print(f'Existem {digitos_certos_posicao_correta} dígito(s) correto(s) e na posição CORRETA.')
        print(f'Existem {digitos_certos_posicao_errada} dígito(s) correto(s), mas na posição ERRADA. ')
        tentativa += 1
    

