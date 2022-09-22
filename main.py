import funcao

matriz= funcao.criaJogo()

venceu=2

funcao.verificacaoVenceu(matriz)
funcao.printarMatriz(matriz)
while(venceu==2):
    jogX=0
    jogO=0
    while(jogX==0):
        x=int(input("Qual casa você quer colocar o X?"))

        if(funcao.verificacaoX(x,matriz)==1):
            matriz=funcao.jogadaX(x,matriz)
            jogX=1
    venceu=funcao.verificacaoVenceu(matriz)
    funcao.printarMatriz(matriz)
    if(venceu!=2):
        break



    while (jogO == 0):
        o = int(input("Qual casa você quer colocar o O?"))

        if (funcao.verificacaoO(o,matriz) == 0):
            matriz = funcao.jogadaO(o, matriz)
            jogO = 1
    venceu=funcao.verificacaoVenceu(matriz)

    funcao.printarMatriz(matriz)


if(venceu==0):
    print("JOGADOR O VENCEU!!!")

elif(venceu==1):
    print("JOGADOR X VENCEU!!!")

elif(venceu==3):
    print("EMPATE!!!")