import csv
import time
def escreve(path):
    maior = 0
    inicio = time.time()
    lista = []
    pathF = path+'.csv'
    with open(pathF) as csvFile:
        num = csv.reader(csvFile, delimiter=';')
        for i in num:
            lista = lista+i
        
        resposta = max(int(maior) for maior in lista)
        print('Maior',resposta)
    fim = time.time()
    
    pathResposta = 'resposta-'+ path+'.txt'
    with open(pathResposta, 'w') as arq:
        tempo = fim-inicio
        tempo = str(tempo)
        m = str(resposta)
        fim = str(fim)
        arq.write(str("Maior:"+m+"\n"))
        arq.write(str("Tempo:"+tempo))
                  
DSa = 'dataset-2-a'
DSb = 'dataset-2-b'
DSc = 'dataset-2-c'
DSd = 'dataset-2-d'
DSe = 'dataset-2-e'

escreve(DSa)
escreve(DSb)
escreve(DSc)
escreve(DSd)
escreve(DSe)
