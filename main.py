import os
import time
import random

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

jogadas = ['pedra', 'papel', 'tesoura']

meu_placar = 0
placar_pc = 0

limpar_tela()
print("")
print("==== BEM-VINDO AO JOGO PEDRA, PAPEL OU TESOURA ====")

while True:
    print("")
    print("------- Placar do Jogo -------")
    print(f"         Você: {meu_placar}      ")
    print(f"         Máquina: {placar_pc}      ")
    print("")

    print("Selecione uma jogada: ")
    minha_jogada = input().lower()

    while minha_jogada not in jogadas:
        print("")
        print("Jogada inválida! Selecione uma jogada válida")
        print("")
        print("Selecione uma jogada: ")
        minha_jogada = input().lower()

    jogada_pc = random.choice(jogadas)

    print("")
    print(f"Sua jogada: {minha_jogada}")
    print(f"jogada da máquina: {jogada_pc}")
    print("")

    if minha_jogada == jogada_pc:
        print("Empate!")
        print("")
    elif (minha_jogada == 'pedra' and jogada_pc == 'tesoura') or \
         (minha_jogada == 'tesoura' and jogada_pc == 'papel') or \
         (minha_jogada == 'papel' and jogada_pc == 'pedra'):
        print("Você venceu esta rodada!")
        print("")
        meu_placar += 1
    else:
        print("Máquina venceu esta rodada!")
        print("")
        placar_pc += 1

    print("Deseja continuar? Se sim, qualquer tecla. Se não, digite 0")
    continuar = input()

    if continuar == '0':
        limpar_tela()
        print("")
        print("Você decidiu encerrar! Obrigado por jogar aqui")
        print("")
        print("------- Placar final -------")
        print(f"         Você: {meu_placar}      ")
        print(f"         Máquina: {placar_pc}      ")
        print("")
        break
    else: 
        print("")
        print("Você decidiu continuar jogando!")
        time.sleep(2)
        limpar_tela()