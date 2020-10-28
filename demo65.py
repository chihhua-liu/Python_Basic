#demo64

# import functools
# import graphviz as gv
#
# graph = functools.partial(gv.Graph, format='svg')
# digraph = functools.partial(gv.Digraph, format='svg')
# g1 = graph()
#
#
# def add_nodes(g, nodes):
#     for n in nodes:
#         if isinstance(n, tuple):
#             pass
#         else:
#             g.node(n)
#     return g
#
#
# def add_edges(g, edges):
#     for e in edges:
#         if isinstance(e[0], tuple):
#             pass
#         else:
#             g.edge(*e)
#     return g
#
#
# nodes1 = ['Toyota', 'Lexus', 'Ford', 'Honda']
# g1 = add_nodes(g1, nodes1)
# edges1 = [('Toyota', 'Lexus'), ('Toyota', 'Honda'), ('Ford', 'Honda')]
# g1 = add_edges(g1, edges1)
# g1.render('graph/demo64_g1')
#------------------------------------------------------
# import functools
# import graphviz as gv
# from itertools import combinations
#
# graph = functools.partial(gv.Graph, format='svg')
# digraph = functools.partial(gv.Digraph, format='svg')
# g1 = graph()
#
#
# def add_nodes(g, nodes):
#     for n in nodes:
#         if isinstance(n, tuple):
#             pass
#         else:
#             g.node(n)
#     return g
#
#
# def add_edges(g, edges):
#     for e in edges:
#         if isinstance(e[0], tuple):
#             pass
#         else:
#             g.edge(*e)
#     return g
#
#
# nodes1 = ['Toyota', 'Lexus', 'Ford', 'Honda']
# g1 = add_nodes(g1, nodes1)
# edges1 = list(combinations(nodes1, 2))
# # edges1 = [('Toyota', 'Lexus'), ('Toyota', 'Honda'), ('Ford', 'Honda')]
# g1 = add_edges(g1, edges1)
# g1.render('graph/demo64_g1')

#-----------------------------------------------------
# demo64'''
# import functools
# import graphviz as gv
# from itertools import combinations
#
# graph = functools.partial(gv.Graph, format='svg')
# digraph = functools.partial(gv.Digraph, format='svg')   #unctools
# g1 = graph()
# g2 = digraph()
#
#
# def add_nodes(g, nodes):
#     for n in nodes:
#         if isinstance(n, tuple):
#             g.node(n[0], **n[1])
#         else:
#             g.node(n)
#     return g
#
#
# def add_edges(g, edges):
#     for e in edges:
#         if isinstance(e[0], tuple):
#             g.edge(*e[0], **e[1])
#         else:
#             g.edge(*e)
#     return g
#
#
# nodes1 = ['Toyota', 'Lexus', 'Ford', 'Honda']
# g1 = add_nodes(g1, nodes1)
# edges1 = list(combinations(nodes1, 2))
# # edges1 = [('Toyota', 'Lexus'), ('Toyota', 'Honda'), ('Ford', 'Honda')]
# g1 = add_edges(g1, edges1)
# g1.render('graph/demo64_g1')
# nodes2 = [('A', {'label': 'Node A'}), ('B', {'label': 'Node B'}),
#           ('C', {'label': '中文的標籤'}), ('D', {})]
# edges2 = [(('A', 'B'), {'label': 'Edge1'}),
#           (('A', 'C'), {'label': 'Edge2'}),
#           (('B', 'C'), {'label': '某種關聯'}),
#           (('B', 'D'), {})]
# g2 = add_nodes(g2, nodes2)
# g2 = add_edges(g2, edges2)
# g2.render('graph/demo64_g2')
# # TB|BT|LR|RL
# styles = {
#     'graph': {
#         'label': 'graphviz於python的使用',
#         'fontsize': '18',
#         'fontcolor': '#000000',
#         'bgcolor': '#C0FFEE',
#         'rankdir': 'RL'
#     }
# }
#
#
# def apply_style(g, s):
#     g.graph_attr.update(('graph' in s and s['graph']) or {})
#     return g
# g3 = apply_style(g2, styles)
# g3.render('graph/demo64_g3')
#-------------------------------------------------------
import functools
import graphviz as gv     # Must install software
from itertools import combinations

graph = functools.partial(gv.Graph, format='svg')

digraph = functools.partial(gv.Digraph, format='svg')

g1 = graph()
g2 = digraph()


def add_nodes(g, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            g.node(n[0], **n[1])
        else:
            g.node(n)
    return g


def add_edges(g, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            g.edge(*e[0], **e[1])
        else:
            g.edge(*e)
    return g


nodes1 = ['Toyota', 'Lexus', 'Ford', 'Honda']
g1 = add_nodes(g1, nodes1)
edges1 = list(combinations(nodes1, 2))
# edges1 = [('Toyota', 'Lexus'), ('Toyota', 'Honda'), ('Ford', 'Honda')]
g1 = add_edges(g1, edges1)
g1.render('graph/demo64_g1')
nodes2 = [('A', {'label': 'Node A'}), ('B', {'label': 'Node B'}),
          ('C', {'label': '中文的標籤'}), ('D', {})]
edges2 = [(('A', 'B'), {'label': 'Edge1'}),
          (('A', 'C'), {'label': 'Edge2'}),
          (('B', 'C'), {'label': '某種關聯'}),
          (('B', 'D'), {})]
g2 = add_nodes(g2, nodes2)
g2 = add_edges(g2, edges2)
g2.render('graph/demo64_g2')
# TB|BT|LR|RL
styles = {
    'graph': {
        'fontname': 'Microsoft Yahei',
        #'fontname': '標楷體',
        'label': 'graphviz於python的使用',
        'fontsize': '18',
        'fontcolor': '#000000',
        'bgcolor': '#C0FFEE',
        'rankdir': 'RL'
    },
    'nodes': {
        'fontname': 'Microsoft Yahei',
        'shape': 'box',
        'fontcolor': 'green',
        'color': 'red',
        'style': 'filled',
        'fillcolor': '#FFC0EE'
    },
    'edges': {
        'style': 'dotted',
        'color': '#002288',
        'arrowhead': 'open',
        'fontname': 'Microsoft Yahei',
        'fontsize': '24',
        'fontcolor': '#220088'
    }
}


def apply_style(g, s):
    g.graph_attr.update(('graph' in s and s['graph']) or {})
    g.node_attr.update(('nodes' in s and s['nodes']) or {})
    g.edge_attr.update(('edges' in s and s['edges']) or {})
    return g


g3 = apply_style(g2, styles)
g3.render('graph/demo64_g3')