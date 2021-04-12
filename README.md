# Proyecto 1 - Biblioteca de generación y manejo de grafos

**INSTITUTO POLITÉCNICO NACIONAL**

**Centro de Investigación en Computación**

**PRESENTA** Victor Christian Jaime Tamayo

**BOLETA** A210232

**ASIGNATURA** Diseño y Análisis de Algoritmos

**PROFESOR** Dr. Rolando Quintero Téllez

**SEMESTRE** A21

**FECHA** 11 de abril de 2021

---

## Instrucciones

Escribir una biblioteca orientada a objetos, en Python 3.6, para describir
y utilizar grafos. Debe, por lo menos contar con una clase llamada Grafo,
una clase llamada Nodo y una clase llamada Arista. Asimismo, se deben
realizar funciones para generar grafos con los siguientes modelos de
generación:

- Modelo Gm,n de **malla**
- Modelo Gn,m de **Erdös y Rényi**
- Modelo Gn,p de **Gilbert**
- Modelo Gn,r **geográfico simple**
- Variante del modelo Gn,d **Barabási-Albert**
- Modelo Gn **Dorogovtsev-Mendes**

La clase grafo debe contar con un método para guardar el grafo en un
archivo con formato **GraphViz** (simple).

Entregar:
1. Link del repositorio en un servidor **GIT** (sugerido **GitHub**)
2. Archivos GV generados, **3** por cada modelo; uno con **30**, otro con
**100** y el tercero con **500** nodos.
3. Imágenes creadas con los grafos generados, **18** en total. Se
sugiere utilizar **Gephi** (https://gephi.org/).

---

## Resultados

- **Archivos GV generados:** [graphviz](/graphviz)

- **Código fuente:** [src](/src)

- **Imágenes:** [img](/img)

- Se utilizó el siguiente script para generar todos los grafos de este proyecto: [ejemplos.py](/src/ejemplos.py)

---

## Modelo Gm,n de malla
- m: número de columnas 
- n: número de filas
- dirigido: el grafo es dirigido

### 30 nodos
**m = 6, n = 5, dirigido = False**

<img src="/img/grafoMalla_m_6_n_5.png" width="500" />

### 100 nodos
**m = 25, n = 4, dirigido = False**

<img src="/img/grafoMalla_m_25_n_4.png" width="500" />

### 500 nodos
**m = 50, n = 10, dirigido = False**

<img src="/img/grafoMalla_m_50_n_10.png" width="500" />

## Modelo Gn,m de Erdös y Rényi
- n: número de nodos (> 0)
- m: número de aristas (>= n-1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

### 30 nodos
**n = 30, m = 30, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_30_m_30.png" width="500" />

### 100 nodos
**n = 100, m = 100, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_100_m_100.png" width="500" />

### 500 nodos
**n = 500, m = 500, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_500_m_500.png" width="500" />

