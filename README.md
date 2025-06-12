# 🔐 Jogo de Adivinhação da Senha (Estilo Cofre)

Este projeto é um simples jogo de terminal em Python onde o jogador tem 5 tentativas para descobrir uma senha secreta de 4 dígitos gerada aleatoriamente.

## 📋 Descrição

O objetivo é adivinhar corretamente todos os 4 dígitos da senha, na ordem certa. A cada tentativa, o programa informa:

- Quantos dígitos estão **corretos e na posição correta**.
- Quantos dígitos estão **corretos, mas em posição errada**.

Após 5 tentativas sem sucesso, o "cofre" é bloqueado.

## 🚀 Como Jogar

1. Execute o script Python.
2. Tente adivinhar a senha digitando uma combinação numérica de 4 dígitos.
3. O programa fornece feedback após cada tentativa.
4. O jogo termina quando:
   - Você acerta todos os 4 dígitos na posição correta.
   - Você atinge o limite de 5 tentativas.

## 💻 Requisitos

- Python 3.x

## ▶️ Execução

No terminal:

```bash
python nome_do_arquivo.py
```

Substitua `nome_do_arquivo.py` pelo nome real do arquivo do script.

## 🧠 Exemplo de Saída

```text
== Tentativa (1/5) ==
Senha: 1234
Existem 1 dígito(s) correto(s) e na posição CORRETA.
Existem 2 dígito(s) correto(s), mas na posição ERRADA.
```

## 📌 Regras

- A senha é composta por 4 dígitos numéricos (entre 0000 e 9999).
- Dígitos podem se repetir.
- Entradas inválidas (não numéricas ou com número incorreto de dígitos) são rejeitadas com mensagens de erro.

## 📂 Estrutura do Código

- `random.randint(0, 9999)`: Gera a senha.
- Conversão para lista de dígitos para comparação.
- Validação da entrada do usuário.
- Contagem de acertos com base em posição e valor.

## 📄 Licença

Este projeto é livre para uso pessoal ou educacional.