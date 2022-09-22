def criaJogo():
    matriz=[]
    for i in range (3):
        linha=[]
        for j in range(3):
            linha.append(9)
        matriz.append(linha)

    return matriz

def verificacaoVenceu(matriz):
    temdois=0
    venceu=2
    diagonal=0
    secundaria=0
    for i in range(3):
        linha=0
        for j in range(3):
            linha+=matriz[i][j]

            if(i==j):
                diagonal+=matriz[i][j]
            if((i+j)==2):
                secundaria+=matriz[i][j]

            if(i==2 and j==2):
                if(linha==0):
                    venceu=0
                    break
                elif(linha==3):
                    venceu=1
                    break
    if (diagonal == 0):
        venceu = 0
    elif (diagonal == 3):
        venceu = 1

    if (secundaria == 0):
        venceu = 0
    elif (secundaria == 1):
        venceu = 1

    if(venceu==0):
        return 0
    elif (venceu == 1):
        return 1

    for j in range(3):
        coluna=0
        for i in range(3):
            coluna+=matriz[i][j]
            if(i==2 and j==2):
                if(coluna==0):
                    venceu=0
                    break
                elif(coluna==3):
                    venceu=1
                    break
    if(venceu==0):
        return 0
    elif (venceu == 1):
        return 1

    for i in range(3):
        for j in range(3):
            if (matriz[i][j] == 9):
                temdois += 1
    if (temdois == 0):
        return 3

    return 2

def qualNum(n):
    x=10
    y=10
    if(n==1):
        x=0
        y=0

    elif(n==2):
        x=0
        y=1

    elif(n==3):
        x=0
        y=2

    elif(n==4):
        x=1
        y=0

    elif(n==5):
        x=1
        y=1

    elif(n==6):
        x=1
        y=2

    elif(n==7):
        x=2
        y=0

    elif(n==8):
        x=2
        y=1

    elif(n==9):
        x=2
        y=2

    return x, y

def verificacaoX(x,matriz):
    coor1,coor2=qualNum(x)
    if(coor1>2 or coor2>2):
        print("Não pode nessa casa, repita a jogada")
        return 2

    if(matriz[coor1][coor2]==9):
        return 1

    else:
        print("Não pode nessa casa, repita a jogada")
        return 2



def verificacaoO(o, matriz):
    coor1, coor2 = qualNum(o)
    if(coor1>2 or coor2>2):
        print("Não pode nessa casa, repita a jogada")
        return 2
    if (matriz[coor1][coor2] == 9):
        return 0

    else:
        print("Não pode nessa casa, repita a jogada")


def jogadaX(x, matriz):
    coor1, coor2 = qualNum(x)


    matriz[coor1][coor2]=1
    return matriz


def jogadaO(o, matriz):
    coor1, coor2 = qualNum(o)
    matriz[coor1][coor2]=0
    return matriz


def printarMatriz(matriz):
    for i in range(3):
        print(matriz[i])

