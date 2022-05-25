from PySimpleGUI import PySimpleGUI as sg
def main():
    x = "bindec"
    y = "decbin"

    tipo = input("Qual conversão deseja, bindec ou decbin? ")
    print(" ")

    if tipo == x:
        try:
            numero = int(input("Qual número binário deseja converter para decimal? "),2)
            a = bin2dec(numero)
            print(a)
            print(" ")
            g = input("Para tentar novamente digite 1: ")
            if g == "1":
                print(" ")
                main()
            else:
                print(" ")
                print("Obrigado por usar meu conversor! ")
                exit()
        except ValueError:
            print(" ")
            print("Valor inválido! ")
            print(" ")
            main()

    if tipo == y:
        try:
            numero2 = int(input("Qual número decimal deseja converter para binário? "))
            b = dec2bin(numero2)
            print(b)
            print(" ")
            g = input("Para tentar novamente digite 1: ")
            if g == "1":
                print("")
                main()
            else:
                print(" ")
                print("Obrigado por usar meu conversor! ")
                exit()
        except ValueError:
            print(" ")
            print("Valor inválido! ")
            print(" ")
            main()



    if tipo != x and tipo != y:
        print("Houve algum erro! Por favor digite novamente: ")
        print(" ")
        main()

def dec2bin(numero2):
    lista = []
    while numero2 >= 2:
        r = numero2 // 2
        q = numero2 % 2
        numero2 = r
        lista.append(q)
    else:
        if numero2 == 1:
            lista.append(1)
        else:
            lista.append(0)
    lista2 = []
    for x in lista[::-1]:
        lista2.append(x)
    return lista2

def bin2dec(numero):
    lista3 = [1]
    lista4 = [int(a) for a in str(numero)]
    #print(lista4)#
    k = str(numero)
    n = len(k)
    an = 1
    while an < 2**(n-1):
        an = an * 2
        #print(an)#
        lista3.append(an)
        #print(lista3)#
    lista5 = []
    for x in lista3[::-1]:
        lista5.append(x)
    produto = [x*y for x,y in zip(lista5,lista4)]
    #print(produto)#
    soma = 0
    for x in produto:
        soma += x
        #print(soma)#
    return soma


#layout
sg.theme('DarkTeal11')
layout = [
    ['',sg.Text('Conversor')],
    [sg.Text('N° Decimal'), sg.Input(key = 'ndecimal'),sg.],
    [sg.Text('N° Binário'), sg.Input(key = 'nbinario')],
    ['', sg.Button('Converter')]
]

#janela
janela = sg.Window('Conversor', layout)

#ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
  #  if eventos == 'Converter'#

#classe
class App():
    def __init__(self):
        self.window = sg.Window('Conversor', layout = layout, return_keyboard_events=False)
        self.result = 0
        self.window.read(timeout=1)
