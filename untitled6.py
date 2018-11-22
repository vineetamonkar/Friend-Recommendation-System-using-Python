# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:45:49 2018

@author: vineet
"""

import pandas as pd


import networkx as nx
import matplotlib.pyplot as plt

p_graph = nx.Graph()

p_graph.add_node("A")
p_graph.add_node("B")
p_graph.add_node("C")
p_graph.add_node("D")
p_graph.add_node("E")
p_graph.add_node("F")

p_graph.add_edge("A","B")
p_graph.add_edge("A","C")
p_graph.add_edge("B","C")
p_graph.add_edge("B","D")
p_graph.add_edge("C","D")
p_graph.add_edge("D","F")
p_graph.add_edge("D","E")
p_graph.add_edge("C","F")


assert len(p_graph.nodes()) == 6
assert len(p_graph.edges()) == 8


nx.draw(p_graph)
plt.show()

