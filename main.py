def main():
    x = "bindec"
    y = "decbin"

    tipo = input("Qual conversão deseja, bindec ou decbin? ")

    if tipo == x:
        numero = int(input("Qual número binário deseja converter para decimal? "))
        a = bin2dec(numero)
        print(a)
    if tipo == y:
        numero2 = int(input("Qual número decimal deseja converter para binário? "))
        b = dec2bin(numero2)
        print(b)
    else:
        print("Obrigado por usar meu Conversor! ")

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
    k = str(numero)
    n = len(k)
    an = 1
    while an <= 2**(n-1):
        an = an * 2
        print(an)
        lista3.append(an)
    soma = 1 #corrigir a multiplicação#
    for x in lista3:
        soma += an
    return soma


main()