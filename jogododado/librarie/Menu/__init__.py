from time import sleep
from jogododado.librarie.fixs import *
from random import randint
from playsound import playsound
saldo = r = 0
def menu(n = 0):
    global saldo
    if n == 0:
         headings('BEM VINDO AO CASSINO !!!', cor='AZUL', l=93)
         while True:
              op = leia_op("QUER SE TORNAR O MAIS NOVO MILIONÁRIO? SIM OU NÃO?")
              if op in 'S':
                  print('JÁ VI QUE VOCÊ É MUITO AMBICIOSO. ENTÃO BOA SORTE E VAMOS JOGAR!!')
                  sleep(3)
                  headings('MODOS DE JOGO', cor='azul', l=93)
                  print(F'{ansi_colors("branco")}ENTÃO DEIXE ME TE EXPLICAR OS MODOS DE JOGO DISPONÍVEIS:')
                  sleep(1)
                  print(
                      f'O MAIS FAMOSO CHAMA-SE {modo("LOW")} AND {modo("HIGH")}. VOCÊ DEVERÁ DIZER {modo("L")} PARA JOGAR {modo("LOW")} OU {modo("H")} PARA JOGAR {modo("HIGH")}.')
                  sleep(3)
                  print(
                      f'LEMBRE QUE {modo("L")} SÃO OS VALORES DO DADO DE 1, 2 E 3 E {modo("H")} OS VALORES DE 4, 5 E 6.')
                  sleep(3)
                  print(
                      f'NESTE MODO, SUAS CHANCES DE GANHAR SÃO ALTAS, PORÉM SEU PRÊMIO SERA DE {modo(1.8)} VEZES O VALOR DA APOSTA. MAS SE PERDER, BOM, VOCÊ JÁ SABE...')
                  sleep(3)
                  print(
                      f'O NOSSO OUTRO ESTILO DE JOGO DISPONÍVEL CHAMA {modo("BLACK AND JACK")}, NO QUAL VOCê DEVERÁ ESCOLHER APENAS UM NÚMERO ENTRE 1 E 6.')
                  sleep(3)
                  print(
                      f'SUAS CHANCES DE GANHAR DIMINUEM NESTE MODO, PORÉM, CASO GANHE, SUA RECOMPENSA SERÁ DE {modo(5)} VEZES A SUA APOSTA.')
                  sleep(3)
                  modo_de_jogo()
              else:
                  print("OK, VOLTE OUTRO DIA :)")
                  sleep(2)
                  print('ALGUMAS HORAS DEPOIS...')
                  sleep(5)
                  print('VOCÊ NÃO ENGANA NINGUÉM! É CLARO QUE VOCÊ QUER JOGAR E SE TORNAR UM MILIONÁRIO.')
    else:
        print_line(n=93, cor='azul')
        op = leia_op('VOCÊ QUER APOSTAR NOVAMENTE?')
        if op in 'N':
            sleep(2)
            print(f'OBRIGADO POR JOGAR CONOSCO. O SEU SALDO FOI DE R${modo(saldo)}, TENHA UM BOM DIA!')
            headings("JOGO DO DADO FINALIZADO", cor ="azul", l=93)
            exit()
        else:
            modo_de_jogo()

def modo_de_jogo():
    global r, saldo
    if r > 0 and saldo > 50:
        print(f'O SEU SALDO É DE R${modo(saldo)}. VOCÊ É OUSADO O BASTANTE PARA ARRISCÁ-LO???')
        sleep(2)
        print('PENSE BEM...')
        sleep(3)
        aposta = leia_real('QUAL VALOR DA SUA APOSTA?')
        saldo-=aposta
    elif r > 0 and saldo <50:
        print(f'O SEU SALDO É DE R${modo(saldo)}. TENTE NOVAMENTE E SAIA LUCRANDO')
        sleep(2)
        print('PENSE BEM...VOCÊ NÃO VAI QUERER IR EMBORA ASSIM')
        sleep(3)
        aposta = leia_real('QUAL VALOR DA SUA APOSTA?')
        saldo -= aposta
    else:
        aposta = leia_real('AGORA DIGA O MAIS IMPORTANTE HEHE, QUAL VALOR DA SUA APOSTA?')
    print(f"E AGORA COM R${modo(aposta)}, COM QUAL MODO DE JOGO VOCÊ PRETENDE MULTIPLICAR ESSE DINHEIRO?")
    sleep(2)
    print(f"{modo('LOW')} AND {modo('HIGH')} OU {modo('BLACK AND JACK')}: ")
    escolha = leia_modo(0)
    print('HMM..')
    sleep(2)
    if escolha == 1:
        print('ÓTIMA ESCOLHA')
        sleep(2)
        dado = randint(1, 6)
        headings('LOW AND HIGH', cor='azul', l=93)
        escolha = leia_modo(f'{ansi_colors("branco")}BOM, AGORA VOCÊ DEVE FAZER SUA APOSTA, LEMBRE QUE {modo("L")} = 1, 2 E 3 E {modo("H")} = 4, 5 E 6. QUAL A SUA ESCOLHA, {modo("L")} OU {modo("H")}? ')
        if escolha in "L":
            escolha = low_high(1, 4)
        else:
            escolha = low_high(4, 7)
        print('RODANDO O DADO...')
        sleep(3)
        print(f'O DADO CAIU NO NÚMERO {dado}')
        r += 1
        if escolha == dado:
            playsound("acerto mizeravi.mp3")
            premio = aposta * 1.8
            saldo += (premio + aposta)
            print(f'PARABÉS VOCÊ GANHOU COMEÇOU COM {modo(aposta)} E ACABOU DE GANHAR RS{modo(premio)}.AGORA O SEU SALDO É DE R${modo(saldo)}')
            print('JA SINTO SEU CHEIRO DE MILIONÁRIO. CONTINUE JOGANDO!!!')
            menu(r)
        else:
            playsound('errou-i-faustao.mp3')
            print(f'VOCê PERDEU R${modo(aposta)} :(. O SEU SALDO É DE R${modo(saldo)}')
            print(f'NÃO FIQUE SE LAMENTANDO, JOGUE NOVAMENTE E DÊ TCHAU PARA O AZAR')
            menu(r)
    else:
        print('O NOSSO LEMA É OUSADIA E ALEGRIA ... BOA ESCOLHA')
        sleep(2)
        dado = randint(1, 6)
        headings(f'{ansi_colors("TÍTULO")}BLACK AND JACK{ansi_colors("AZUL")}{ansi_colors("padrão")}{ansi_colors("azul")}', cor='azul', l=93)
        print(f'{ansi_colors("branco")}AGORA VOCÊ DEVE LEMBRAR QUE APENAS GANHARÁ SE O SEU NÚMERO ESCOLHIDO FOR IGUAL AO DO DADO. VOCÊ PODERÁ ESCOLHER QUALQUER NÚMERO DE 1 A 6.')
        sleep(3)
        escolha = low_high(1,7)
        print('RODANDO O DADO...')
        sleep(3)
        print(f'O DADO CAIU NO NÚMERO {dado}')
        r += 1
        if escolha == dado:
            playsound("acerto mizeravi.mp3")
            premio = aposta * 5
            saldo += (premio + aposta)
            print(f'PARABÉS VOCÊ GANHOU! COMEÇOU COM {modo(aposta)} E ACABOU DE GANHAR RS{modo(premio)}.O SEU SALDO É DE R${modo(saldo)}')
            print('JA SINTO SEU CHEIRO DE MILIONÁRIO. CONTINUE JOGANDO!!!')
            menu(r)
        else:
            playsound('errou-i-faustao.mp3')
            print(f'VOCê PERDEU R${modo(aposta)} :(. O SEU SALDO É DE R${modo(saldo)}')
            print(f'NÃO FIQUE SE LAMENTANDO, JOGUE NOVAMENTE E DÊ TCHAU PARA O AZAR')
            menu(r)








