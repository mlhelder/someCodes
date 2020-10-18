SIZE = 5
MIN = -1
INVALIDATED = -1
def policiaLadrao(x,y):
    if(x >= SIZE or y >= SIZE or x <= MIN or y <= MIN or matriz[x][y] == 1 or matriz[x][y] == INVALIDATED):
        return
    else:
        matriz[x][y] = INVALIDATED
        policiaLadrao(x+1 ,y)
        policiaLadrao(x, y+1)
        policiaLadrao(x, y-1)
        policiaLadrao(x-1, y)
        
T = int(input())
i = 0
base = 0
notPass = 1
for i in range(T):
    matriz = []
    while len(matriz) < SIZE :
        linha = list(map(int, input().split()))
        if(len(linha) > base):
            matriz.append(linha)
            
    #checagem inicial 
    if( matriz[base][base] == notPass or matriz[4][4] == notPass or (matriz[3][4] == notPass and matriz[4][3] == notPass)):
        print("ROBBERS")
    else:
        policiaLadrao(base,base)
        fugiu = matriz[4][4] != INVALIDATED
        if(fugiu):
            print("ROBBERS")
        else:
            print("COPS")
