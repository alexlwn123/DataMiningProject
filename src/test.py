import pandas as pd
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
from matplotlib import pylab
import numpy as np
import networkx as nx

def save_graph(graph,file_name):
  #initialze Figure
  plt.figure(num=None, figsize=(20, 20), dpi=80)
  plt.axis('off')
  fig = plt.figure(1)
  pos = nx.spring_layout(graph)
  nx.draw_networkx_nodes(graph,pos)
  nx.draw_networkx_edges(graph,pos)

  cut = 1.00
  xmax = cut * max(xx for xx, yy in pos.values())
  ymax = cut * max(yy for xx, yy in pos.values())
  plt.xlim(0, xmax)
  plt.ylim(0, ymax)

  plt.savefig(file_name,bbox_inches="tight")
  pylab.close()
  del fig
def main():
  data_directed = pd.read_csv("data\class_data\CA-GrQc.txt", sep="\t")
  citeseer_data = pd.read_csv("data\ca-citeseer\ca-citeseer.mtx", sep=" ")
  citeseer_cites = pd.read_csv("data\citeseer\citeseer.cites", sep = "\t")
  citeseer_content = pd.read_csv("data\citeseer\citeseer.content", sep = "\t")
  data_undirected = pd.read_csv("data\class_data\com-dblp.ungraph.txt", sep="\t")
  G = nx.read_edgelist("data\class_data\CA-GrQc.txt", nodetype=int)
  
    
# drawing in circular layout 
  #nx.draw_circular(G, pos=pos, with_labels = True) 
  #print(citeseer_data)
  #print(data_directed)
  #print(data_undirected)
  #print(nx.from_pandas_edgelist(citeseer_data))

  #G = nx.Graph()
  #graph = nx.from_pandas_adjacency(data_undirected)
  save_graph(G, "bad_project.pdf")

  first_col = data_undirected.iloc[:,0]
  second_col =  data_undirected.iloc[:,1]
  reverse = pd.concat([second_col, first_col], axis=1)
  symmetric_undirected = pd.concat([data_undirected, reverse]).reset_index()


  counts = first_col[:1000].value_counts()
  counts.plot.bar()
  plt.show()

if __name__ == '__main__':
  main()
