def removeLetras(palavra):
    Dicionario = {}
    for letra in palavra:
        prevKeys = list(Dicionario.keys())
        for chave in prevKeys:
            if((chave + letra) not in Dicionario):
                Dicionario[chave + letra] = True
        if(letra not in Dicionario):
            Dicionario[letra] = True
        
    for chave in sorted(Dicionario.keys()):
        print(chave)
    print()

try:
    while 1:
        removeLetras(input())
except:
    pass
