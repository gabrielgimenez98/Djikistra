grafo = { "A" : { "B" : 1, "C":2 },
          "B" : { "D":2, "E":4 },
          "C" : { "E":2 },
          "D" : { "F": 6 },
          "E" : { "F": 7 },
          "F" : { }
          }

grafo2 = {  "D" : { "A": 4, "H": 1 },
            "A" : { "H": 10, "E": 1 },
            "H" : { "E": 5, "I": 9 },
            "E" : { "F" : 3 },
            "I" : { "J" : 2 },
            "F" : { "I" : 1, "G": 7, "B": 1, "C": 3 },
            "G" : { },
            "J" : { "G" : 1 },
            "B" : { "C" : 2 },
            "C" : { } }
            

def dijkstra_path(grafo, origem, fim): #retorna a menor distancia de um No origem até um No destino e o caminho até ele

    controle = { }
    distanciaAtual = { }
    noAtual = { }
    naoVisitados = []
    atual = origem
    noAtual[atual] = 0

    
    for vertice in grafo.keys():
        naoVisitados.append(vertice) #inclui os vertices nos não visitados    
        distanciaAtual[vertice] = float('inf') #inicia os vertices como infinito

    distanciaAtual[atual] = [0,origem] 

    naoVisitados.remove(atual)

    while naoVisitados:
        for vizinho, peso in grafo[atual].items():
             pesoCalc = peso + noAtual[atual]
             if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho][0] > pesoCalc:
                 distanciaAtual[vizinho] = [pesoCalc,atual]
                 controle[vizinho] = pesoCalc
                 print(controle)
                 
        if controle == {} : break    
        minVizinho = min(controle.items(), key=lambda x: x[1]) #seleciona o menor vizinho
        atual=minVizinho[0]
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]

    print("A menor distância de %s atá %s é: %s" % (origem, fim, distanciaAtual[fim][0]))
    print("O menor caminho é: %s" % printPath(distanciaAtual,origem, fim))          
    

def printPath(distancias,inicio, fim):
        if  fim != inicio:
            return "%s -- > %s" % (printPath(distancias,inicio, distancias[fim][1]),fim)
        else:
            return inicio

def input_data(tamanho_grafo):
    lst_full = ["A","B","C","D","E","F","G","H","I","J","K"]

    return [lst_full[x] for x in range(tamanho_grafo)]

# dijkstra_path(grafo,"A","F")

tamanho_grafo = int(input("Digite a quantidade de vertices de o grafo tera\n"))

lista = input_data(tamanho_grafo)