import graphviz as gv

# make a directory graph
# svg|pdf|png
g1 = gv.Graph(format='png')
#g1 = gv.Digraph(format='png')
g1.node('A')
g1.node('B')
g1.edge('A', 'A')
g1.edge('A', 'B')
g1.edge('B', 'B')
g1.edge('B', 'B')
print(g1.source)
g1.render('graph/demo63')