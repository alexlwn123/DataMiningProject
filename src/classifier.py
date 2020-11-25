import sys
import matplotlib.pyplot as plt
from matplotlib import pylab
import networkx as nx

def save_graph(graph,file_name):
  #initialze Figure
  plt.figure(num=None, figsize=(20, 20), dpi=80)
  plt.axis('off')
  fig = plt.figure(1)
  pos = nx.spring_layout(graph)
  nx.draw_networkx_nodes(graph,pos)
  nx.draw_networkx_edges(graph,pos)

  plt.savefig(file_name,bbox_inches="tight")
  pylab.close()
  del fig

def find(uf, u):
  """
  Test uf = u
  >>> find([0, 1], 1)
  1

  Test uf != u
  >>> find([0, 1], 0)
  0
  """
  if u == uf[u]:
    return uf[u]

  uf[u] = find(uf, uf[u])
  return uf[u]

def union(u, v, uf, size):
  """
  Test None:
  >>> union(4, 5, [1, 1, 1], [1, 2, 3])
  """
  ur, vr = find(uf, u), find(uf, v)
  if ur == vr:
    return 

  if size[ur] > size[vr]:
    size[ur] += size[vr]
    uf[vr] = ur
    find(uf, v)

  else:
    size[vr] += size[ur]
    uf[ur] = vr
    find(uf, u)

def main():
  #G = nx.read_edgelist("data\class_data\CA-GrQc.txt", nodetype=int)
  #save_graph(G, "plot.pdf")
  X = int(input("input number for D: "))

  with open("data\class_data\CA-GrQc.txt", 'r') as f:
    lines = f.read().splitlines()
  
  lines = [list(map(int, line.split())) for line in lines]
  counts = [0] * 30000
  uf = [i for i in range(30000)]
  size = [1] * len(uf)
  for line in lines:
    counts[line[0]] += 1
    counts[line[1]] += 1
    union(find(uf, line[0]), find(uf, line[1]), uf, size)
  
  head = size.index(max(size))
  members = [x for x in range(len(uf)) if find(uf, x) == head]
  more = [x for x in range(len(uf)) if counts[x] >= X and find(uf, x) == head]
  hasX = [x for x in range(len(uf)) if counts[x] >= X]
  not_in_cluster = [x for x in range(len(uf)) if find(uf, x) != head and counts[x] >= 1]
  not_in_cluster_with3 = [x for x in range(len(uf)) if find(uf, x) != head and counts[x] >= X]


  print(f"Not in cluster (Negative Coverage): {len(not_in_cluster)}")
  print(f"Not in cluster with {X} neighbors (Incorrect Negative Classifications): {len(not_in_cluster_with3)}")
  print(f"Ratio (negatives that trigger the rule): {len(not_in_cluster_with3)*100/len(not_in_cluster):.3f} %")
  print(f"Ratio (negative accuracy): {100 - len(not_in_cluster_with3)*100/len(not_in_cluster):.3f} %")
  print(f"Has {X} neighbors (Positive Coverage): {len(hasX)}")
  print(f"Has {X} neighbors and is in large cluster (Positive Classifications): {len(more)}")
  print(f"In large cluster: {len(members)}")
  print(f"Ratio: {len(more)*100/len(members):.3f} %")

    
  #first_col = data_undirected.iloc[:,0]
  #second_col =  data_undirected.iloc[:,1]
  #reverse = pd.concat([second_col, first_col], axis=1)
  #symmetric_undirected = pd.concat([data_undirected, reverse]).reset_index()


  #counts = first_col[:1000].value_counts()
  #counts.plot.bar()
  #plt.show()

if __name__ == '__main__':
  import timeit
  main()
  #print(timeit.timeit("main()"))
