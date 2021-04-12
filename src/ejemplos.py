from grafoMalla import grafoMalla
#******************************************************************************
#grafoMalla - 30 nodos
gfMalla = grafoMalla(6,5,dirigido=False)
gfMalla.display()
gfMalla.graphviz()

#grafoMalla - 100 nodos
gfMalla = grafoMalla(25,4,dirigido=False)
gfMalla.display()
gfMalla.graphviz()

#grafoMalla - 500 nodos
gfMalla = grafoMalla(50,10,dirigido=False)
gfMalla.display()
gfMalla.graphviz()
#******************************************************************************

from grafoErdosRenyi import grafoErdosRenyi
#******************************************************************************
#grafoErdosRenyi - 30 nodos
gfErdosReny = grafoErdosRenyi(n=30, m=30, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphviz()

#grafoErdosRenyi - 100 nodos
gfErdosReny = grafoErdosRenyi(n=100, m=100, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphviz()

#grafoErdosRenyi - 500 nodos
gfErdosReny = grafoErdosRenyi(n=500, m=500, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphviz()
#******************************************************************************


from grafoGilbert import grafoGilbert
#******************************************************************************
#grafoGilbert - 30 nodos
gfGilbert = grafoGilbert(n=30, p=0.1, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.graphviz()

#grafoGilbert - 100 nodos
gfGilbert = grafoGilbert(n=100, p=0.1, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.graphviz()

#grafoGilbert - 500 nodos
gfGilbert = grafoGilbert(n=500, p=0.03, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.graphviz()
#******************************************************************************

from grafoGeografico import grafoGeografico
#******************************************************************************
#grafoGeografico - 30 nodos
gfGeografico = grafoGeografico(n=30, r=0.3, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.graphviz()

#grafoGeografico - 100 nodos
gfGeografico = grafoGeografico(n=100, r=0.3, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.graphviz()

#grafoGeografico - 500 nodos
gfGeografico = grafoGeografico(n=500, r=0.1, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.graphviz()
#******************************************************************************

from grafoBarabasiAlbert import grafoBarabasiAlbert
#******************************************************************************
#grafoBarabasiAlbert - 30 nodos
gfBarabasiAlbert = grafoBarabasiAlbert(n=30, d=4, dirigido=False, auto=False)
gfBarabasiAlbert.display()
gfBarabasiAlbert.graphviz()

#grafoBarabasiAlbert - 100 nodos
gfBarabasiAlbert = grafoBarabasiAlbert(n=100, d=4, dirigido=False, auto=False)
gfBarabasiAlbert.display()
gfBarabasiAlbert.graphviz()

#grafoBarabasiAlbert - 500 nodos
gfBarabasiAlbert = grafoBarabasiAlbert(n=500, d=4, dirigido=False, auto=False)
gfBarabasiAlbert.display()
gfBarabasiAlbert.graphviz()
#******************************************************************************

from grafoDorogovtsevMendes import grafoDorogovtsevMendes
#******************************************************************************
#grafoBarabasiAlbert - 30 nodos
gfDorogovtsevMendes = grafoDorogovtsevMendes(30,dirigido=False)
gfDorogovtsevMendes.display()
gfDorogovtsevMendes.graphviz()

#grafoBarabasiAlbert - 100 nodos
gfDorogovtsevMendes = grafoDorogovtsevMendes(100,dirigido=False)
gfDorogovtsevMendes.display()
gfDorogovtsevMendes.graphviz()

#grafoBarabasiAlbert - 500 nodos
gfDorogovtsevMendes = grafoDorogovtsevMendes(500,dirigido=False)
gfDorogovtsevMendes.display()
gfDorogovtsevMendes.graphviz()
#******************************************************************************
