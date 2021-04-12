from Nodo import Nodo
from Arista import Arista
#******************************************************************************
import os
#******************************************************************************
#Clase Grafo
class Grafo:
    def __init__(self,id="grafo",dirigido=False, auto=False):
        self.id=id
        self.nodos={}
        self.aristas={}
        self.dirigido=dirigido
        self.auto=auto

    def agregar_nodo(self, id):
        nuevo_nodo = Nodo(id)
        self.nodos[nuevo_nodo.id]=nuevo_nodo

    def agregar_arista(self,source,target):
        try:
            nueva_arista = Arista(self.nodos[source],self.nodos[target])
            self.aristas[nueva_arista.id]=nueva_arista
            self.nodos[source].grado+=1 #aumentar el grado del nodo
            self.nodos[target].grado+=1 #aumentar el grado del nodo
        except:
            print('***Error - Checar que los nodos se hayan decalarado previamente!***')

    def calcularGrado(self, nodo):
        return self.nodos[nodo].grado

    def totalNodos(self):
        return len(self.nodos)

    def totalAristas(self):
        return len(self.aristas)

    def checarSiAristaExiste(self,source,target):
        nueva_arista = Arista(self.nodos[source],self.nodos[target])
        nueva_arista2 = Arista(self.nodos[target],self.nodos[source])
        if nueva_arista.id in self.aristas:
            return True
        if(not self.dirigido): #Si no es un grafo dirigido
            if nueva_arista2.id in self.aristas:
                return True
        return False


    def nodosConectados(self,nodo):
        nodos_conectados=[]
        for key, value in self.aristas.items():
            if(value.source == self.nodos[nodo]):
                nodos_conectados.append(str(value.target))
            if(not self.dirigido): #Si no es un grafo dirigido
                if(value.target==self.nodos[nodo]):
                    nodos_conectados.append(str(value.source))
        return nodos_conectados

    def graphviz(self):
        contenido=''
        contenido+='digraph '+self.id+' {\n'
        if not self.dirigido:
            contenido+='edge [dir=none, color=purple3]\n'
        else:
            contenido+='edge [color=purple3]\n'

        for nodo in self.nodos: #imprimir nodos
            contenido+=str(nodo)+';\n'

        for key, value in self.aristas.items(): #imprimir aristas
            contenido+= value.id+';\n'

        contenido+='}'

        nombre_completo=self.id+'.gv'
        f = open(nombre_completo, "w")
        f.write(contenido)
        f.close()
        print('Arhivo Graphviz generado: '+nombre_completo+'\n')

    def display(self):
        print('---'+str(self.totalNodos())+' Nodos---')
        print('---'+str(self.totalAristas())+' Aristas---')
#******************************************************************************
