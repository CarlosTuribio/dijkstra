def getGrafo():
    grafo = { "A" : { "B" : 185, "C":119, "D":152, "E":133 },
              "B" : { "A" : 185, "C":121, "D":150, "E":200  },
              "C" : { "A" : 119, "B":121, "D":174, "E":120  },
              "D" : { "A" : 152, "B":150, "C":174, "E":199  },
              "E" : { "A" : 133, "B":200, "C":120, "D":199  }
              }
    return grafo
def chooseVertex(grafo):
    v=[]
    naoVisitados = []
    print("Vertices disponiveis: ")
    for vertice in grafo.keys():
        naoVisitados.append(vertice)
        print(vertice," ", end="")
    v.append(input("\nEscolha o Vertice de partida: "))
    naoVisitados.remove(v[0])
    v.append(naoVisitados)
    return v
def printCaminho(grafo,v):
    print("Menor caminho partindo de (A):\n")
    print(v[0],"=> ", end="")
    dijkstra(grafo,v[0],v[0],v[1],0)

def dijkstra(grafo,origem,etern,naoVisitados,cont):
    meno=float("inf")
    men="A"
    cont=cont
    i=0
    x=0
    if len(naoVisitados)!=0:
        for i in naoVisitados:
            if meno > grafo[origem][i]:
                meno = x = grafo[origem][i]
                men = i
        cont=cont+x
        print(men,"=> ", end="")
        naoVisitados.remove(men)
        return dijkstra(grafo,men,etern,naoVisitados,cont)
    else:
        naoVisitados.append(etern)
        for i in naoVisitados:
            if meno > grafo[origem][i]:
                meno = x = grafo[origem][i]
                men = i
        cont=cont+x
        print(men)
        print("Menor caminho:",cont,"Km")
        return 
