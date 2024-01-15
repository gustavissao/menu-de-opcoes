from time import sleep
v1 = int(input('primeiro valor: '))
v2 = int(input('segundo valor: '))
menu = 0
while menu != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    menu = int(input('<<<<<<< Qual é a sua opção? '))
    if menu == 1:
        soma = v1 + v2
        print(f'A soma entre {v1} + {v2} é {soma}')
    elif menu == 2:
        multiplicar = v1 * v2
        print(f'O resultado entre {v1} x {v2} é {multiplicar}')
    elif menu == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print(f'Entre {v1} e {v2} o maior valor é {maior}')
    elif menu == 4:
        print('Informe os números novamente: ')
        v1 = int(input('primeiro valor: '))
        v2 = int(input('segundo valor: '))
    elif menu == 5:
        print('finalizando...')
    else:
        print('Opçõa invalida. tente novamente.')
    print('++-++' * 10)
    sleep(2)
print('Fim do programa!')