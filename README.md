# Proyecto 1 - Biblioteca de generación y manejo de grafos

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

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

**Código Python:** 
```
from grafoMalla import grafoMalla
gfMalla = grafoMalla(6,5,dirigido=False)
gfMalla.display()
gfMalla.graphviz()
```

<img src="/img/grafoMalla_m_6_n_5.png" width="500" />

> 30 Nodos y 49 Aristas

### 100 nodos
**m = 25, n = 4, dirigido = False**

**Código Python:** 
```
from grafoMalla import grafoMalla
gfMalla = grafoMalla(25,4,dirigido=False)
gfMalla.display()
gfMalla.graphviz()
```

<img src="/img/grafoMalla_m_25_n_4.png" width="500" />

> 100 Nodos y 171 Aristas

### 500 nodos
**m = 50, n = 10, dirigido = False**

**Código Python:** 
```
from grafoMalla import grafoMalla
gfMalla = grafoMalla(50,10,dirigido=False)
gfMalla.display()
gfMalla.graphviz()
```

<img src="/img/grafoMalla_m_50_n_10.png" width="500" />

> 500 Nodos y 940 Aristas
 
---

## Modelo Gn,m de Erdös y Rényi
- n: número de nodos (> 0)
- m: número de aristas (>= n-1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

### 30 nodos
**n = 30, m = 30, dirigido = False, auto=False**

**Código Python:** 
```
from grafoErdosRenyi import grafoErdosRenyi
gfErdosReny = grafoErdosRenyi(n=30, m=30, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphviz()
```

<img src="/img/grafoErdosRenyi_n_30_m_30.png" width="500" />

> 30 Nodos y 30 Aristas

### 100 nodos
**n = 100, m = 100, dirigido = False, auto=False**

**Código Python:** 
```
from grafoErdosRenyi import grafoErdosRenyi
gfErdosReny = grafoErdosRenyi(n=100, m=100, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphviz()
```

<img src="/img/grafoErdosRenyi_n_100_m_100.png" width="500" />

> 100 Nodos y 100 Aristas

### 500 nodos
**n = 500, m = 500, dirigido = False, auto=False**

**Código Python:** 
```
from grafoErdosRenyi import grafoErdosRenyi
gfErdosReny = grafoErdosRenyi(n=500, m=500, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphviz()
```

<img src="/img/grafoErdosRenyi_n_500_m_500.png" width="500" />

> 500 Nodos y 500 Aristas

---

## Modelo Gn,p de **Gilbert**
- n: número de nodos (> 0)
- p: probabilidad de crear una arista (0, 1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

### 30 nodos
**n = 30, p = 0.1, dirigido = False, auto=False**

**Código Python:** 
```
from grafoGilbert import grafoGilbert
gfGilbert = grafoGilbert(n=30, p=0.1, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.graphviz()
```

<img src="/img/grafoGilbert_n_30_p_10.png" width="500" />

> 30 Nodos y 75 Aristas

### 100 nodos
**n = 100, p = 0.1, dirigido = False, auto=False**

**Código Python:** 
```
from grafoGilbert import grafoGilbert
gfGilbert = grafoGilbert(n=100, p=0.1, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.graphviz()
```

<img src="/img/grafoGilbert_n_100_p_10.png" width="500" />

> 100 Nodos y 915 Aristas

### 500 nodos
**n = 500, p = 0.03, dirigido = False, auto=False**

**Código Python:** 
```
from grafoGilbert import grafoGilbert
gfGilbert = grafoGilbert(n=500, p=0.03, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.graphviz()
```

<img src="/img/grafoGilbert_n_500_p_3.png" width="500" />

> 500 Nodos y 7,263 Aristas

---

## Modelo Gn,r **geográfico simple**
- n: número de nodos (> 0)
- r: distancia máxima para crear un nodo (0, 1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

### 30 nodos
**n = 30, r = 0.3, dirigido = False, auto=False**

**Código Python:** 
```
from grafoGeografico import grafoGeografico
gfGeografico = grafoGeografico(n=30, r=0.3, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.graphviz()
```

<img src="/img/grafoGeografico_n_30_r_3.png" width="500" />

> 30 Nodos y 92 Aristas

### 100 nodos
**n = 100, r = 0.3, dirigido = False, auto=False**

**Código Python:** 
```
from grafoGeografico import grafoGeografico
gfGeografico = grafoGeografico(n=100, r=0.3, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.graphviz()
```

<img src="/img/grafoGeografico_n_100_r_3.png" width="500" />

> 100 Nodos y 999 Aristas

### 500 nodos
**n = 500, r = 0.1, dirigido = False, auto=False**

**Código Python:** 
```
from grafoGeografico import grafoGeografico
gfGeografico = grafoGeografico(n=500, r=0.1, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.graphviz()
```

<img src="/img/grafoGeografico_n_500_r_1.png" width="500" />

> 500 Nodos y 3,420 Aristas

---

## Variante del modelo Gn,d **Barabási-Albert**
- n: número de nodos (> 0)
- d: grado máximo esperado por cada nodo (> 1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

### 30 nodos
**n = 30, d = 4, dirigido = False, auto=False**

**Código Python:** 
```
from grafoBarabasiAlbert import grafoBarabasiAlbert
gfBarabasiAlbert = grafoBarabasiAlbert(n=30, d=4, dirigido=False, auto=False)
gfBarabasiAlbert.display()
gfBarabasiAlbert.graphviz()
```

<img src="/img/grafoBarabasiAlbert_n_30_d_4.png" width="500" />

> 30 Nodos y 58 Aristas

### 100 nodos
**n = 100, d = 4, dirigido = False, auto=False**

**Código Python:** 
```
from grafoBarabasiAlbert import grafoBarabasiAlbert
gfBarabasiAlbert = grafoBarabasiAlbert(n=100, d=4, dirigido=False, auto=False)
gfBarabasiAlbert.display()
gfBarabasiAlbert.graphviz()
```

<img src="/img/grafoBarabasiAlbert_n_100_d_4.png" width="500" />

> 100 Nodos y 197 Aristas

### 500 nodos
**n =500, d = 4, dirigido = False, auto=False**

**Código Python:** 
```
from grafoBarabasiAlbert import grafoBarabasiAlbert
gfBarabasiAlbert = grafoBarabasiAlbert(n=500, d=4, dirigido=False, auto=False)
gfBarabasiAlbert.display()
gfBarabasiAlbert.graphviz()
```

<img src="/img/grafoBarabasiAlbert_n_500_d_4.png" width="500" />

> 500 Nodos y 999 Aristas

---

## Modelo Gn **Dorogovtsev-Mendes**
- n: número de nodos (≥ 3)
- dirigido: el grafo es dirigido?

### 30 nodos
**n = 30, dirigido = False**

**Código Python:** 
```
from grafoDorogovtsevMendes import grafoDorogovtsevMendes
gfDorogovtsevMendes = grafoDorogovtsevMendes(30,dirigido=False)
gfDorogovtsevMendes.display()
gfDorogovtsevMendes.graphviz()
```

<img src="/img/grafoDorogovtsevMendes_n_30.png" width="500" />

> 30 Nodos y 57 Aristas

### 100 nodos
**n = 100, dirigido = False**

**Código Python:** 
```
from grafoDorogovtsevMendes import grafoDorogovtsevMendes
gfDorogovtsevMendes = grafoDorogovtsevMendes(100,dirigido=False)
gfDorogovtsevMendes.display()
gfDorogovtsevMendes.graphviz()
```

<img src="/img/grafoDorogovtsevMendes_n_100.png" width="500" />

> 100 Nodos y 197 Aristas

### 500 nodos
**n = 500, dirigido = False**

**Código Python:** 
```
from grafoDorogovtsevMendes import grafoDorogovtsevMendes
gfDorogovtsevMendes = grafoDorogovtsevMendes(500,dirigido=False)
gfDorogovtsevMendes.display()
gfDorogovtsevMendes.graphviz()
```

<img src="/img/grafoDorogovtsevMendes_n_500.png" width="500" />

> 500 Nodos y 997 Aristas

---
