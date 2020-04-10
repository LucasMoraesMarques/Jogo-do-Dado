def ansi_colors(color = 'PADRÃO'):
   """
   Função que simplifica o código Ansi para cores no terminal do python.
   :param color: Recebe a cor de forma nominal.
   :return: Retorna o código \033[-;-;m correspondente a cor.
   """""
   colors = {'PADRÃO':'\033[m', 'BRANCO': "\033[1;30m", 'VERMELHO': "\033[1;31m", 'VERDE': "\033[1;32m", 'AMARELO': "\033[1;33m", 'AZUL': "\033[1;34m", 'MAGENTA': "\033[1;35m", 'CIANO': "\033[1;36m", 'CINZA': '\033[1;37m', 'TÍTULO':'\033[1;31;107m'}
   for k, v in colors.items():
       if color.strip().upper() == k:
           return v

def print_msg_line(msg, cor='PADRÃO'):
    """
    Função que retorna um heading estilístico.
    Ex.:   -=-=-=-=-=-=
              PYTHON
           -=-=-=-=-=-=
    :param msg: Recebe a string a ser formatada.(OBRIGATÓRIO)
    :param cor: Recebe uma cor nominal segundo a função ansi_colors.(OPCIONAL: O default é o padrão da função ansi_colors)
    :return: Retorna o heading formatado com a string e sua respectiva cor.
    """
    n = ansi_colors(cor)
    msg = str(msg)
    l = len(msg)
    if l % 2 == 0:
        return print(f'{n}{"-=" * ((l // 2) + 2)}\n{msg.center(l + 4)}\n{"-=" * ((l // 2) + 2)}{ansi_colors("PADRÃO")}')
    else:
        return print(f'{n}{"-=" * (l)}\n{msg.center(l*2 )}\n{"-=" * (l)}{ansi_colors("PADRÃO")}')

def headings(msg,cor = 'BRANCO', l =20):
    return print(f'{ansi_colors(cor)}{"-=" *l }\n{msg.center(l*2)}\n{"-=" * l }{ansi_colors("padrão")}')

def print_line(n, cor = 'Padrão'):
    return print((f"{ansi_colors(cor)}{'-='*n}{ansi_colors()}"))

def modo(msg):
    if type(msg) == str and msg in 'LLOW':
        return (f'{ansi_colors("vermelho")}{msg}{ansi_colors("branco")}')
    elif type(msg) == str and msg in 'HHIGH':
        return (f'{ansi_colors("VERDE")}{msg}{ansi_colors("branco")}')
    elif type(msg) != str:
        return (f'{ansi_colors("magenta")}{msg:.2f}{ansi_colors("branco")}')
    else:
        return (f'{ansi_colors("TÍTULO")}{msg}{ansi_colors("padrão")}{ansi_colors("branco")}')



