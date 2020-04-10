from jogododado.librarie.Interface import *

def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{ansi_colors("vermelho")}ERRO! Digite um número inteiro válido.{ansi_colors("branco")}')
            continue
        except KeyboardInterrupt:
            print(f'{ansi_colors("vermelho")}{"O usuário preferiu não digitar esse número"}{ansi_colors("branco")}')
            return 0
        else:
            return n


def leia_real(msg):
    while True:
        try:
            n = float(input(f'{ansi_colors("branco")}{msg}'))
        except (ValueError, TypeError):
            print(f'{ansi_colors("vermelho")}ERRO! Digite um número real válido.{ansi_colors("branco")}')
        except KeyboardInterrupt:
            print(f'{ansi_colors("vermelho")}{"O usuário preferiu não digitar esse número"}{ansi_colors("branco")}')
            return 0
        else:
            return n


def leia_op(msg):
    op = 'a'
    while op not in 'SN':
        op = str(input(f'{ansi_colors("branco")}{msg}')).strip().upper()[0]
        if op not in 'SN':
            print(f'{ansi_colors("vermelho")}Opção inválida! Tente novamente, digitando sim ou não{ansi_colors("branco")}')
        else:
            return op


def leia_modo(msg):
    if type(msg) == str:
        op = 'a'
        while op not in 'HL' :
            op = str(input(f'{msg}')).strip().upper()[0]
            if op not in 'HL':
                print(f'{ansi_colors("vermelho")}Modo inválido! Tente novamente.{ansi_colors("branco")}')
            else:
                return op
    else:
        op = 0
        while op not in range(1, 3):
            op = leia_int(
                f'''PARA O MODO {modo("LOW")} AND {modo("HIGH")} DIGITE 1. SE A SUA ESCOLHA FOR O OUSADO MODO {modo("BLACK AND JACK")}, DIGITE 2: ''')
            if op not in range(1, 3):
                print(f'{ansi_colors("vermelho")}Modo inválido! Tente novamente.{ansi_colors("branco")}')
            else:
                return op


def low_high(i, f):
    escolha = 0
    while True:
        try:
            escolha = int(input("Escolha o número: "))
        except(TypeError, ValueError):
            print(f'{ansi_colors("vermelho")}ERRO! Digite um número válido para a opção escolhida{ansi_colors("branco")}')
        if escolha not in range(i, f):
            print(f'{ansi_colors("vermelho")}ERRO! Digite um número válido para a opção escolhida{ansi_colors("branco")}')
        else:
            return escolha
