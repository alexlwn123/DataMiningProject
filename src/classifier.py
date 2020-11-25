import sys
import matplotlib.pyplot as plt
from matplotlib import pylab
import networkx as nx

def save_graph(graph,file_name):
  '''
  Implements networkx to plot graph data. 
  Saves plot to file name.
  '''
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
  Finds parent of node u. Implements path compression for efficiency.

  Test uf = u
  >>> find([0, 1], 1)
  1

  Test uf != u
  >>> find([2, 1, 1], 0)
  1
  """
  if u == uf[u]:
    return uf[u]

  uf[u] = find(uf, uf[u])
  return uf[u]


def union(u, v, uf, size):
  """
  Unions disjoint sets cointining nodes u and v. 
  Follows Union-by-size for efficiency.

  Test uniform:
  >>> union(0, 1, [0,1,2], [1,1,1])
  [1, 1, 2]

  Test u is bigger:
  >>> union(0, 2, [0,0,2], [2,1,1])
  [0, 0, 0]

  Test v is bigger:
  >>> union(2, 0, [0,0,2], [2,1,1])
  [0, 0, 0]

  Test v and u are already unioned:
  >>> union(0, 1, [0,0,2], [2,1,1])
  [0, 0, 2]
  """
  ur, vr = find(uf, u), find(uf, v)
  if ur == vr:
    return uf

  if size[ur] > size[vr]:
    size[ur] += size[vr]
    uf[vr] = ur
    find(uf, v)
    return uf

  else:
    size[vr] += size[ur]
    uf[ur] = vr
    find(uf, u)
    return uf

def getMicroF1(tp, fp, fn): 
  '''
  Calculates the Micro-F1 score for classification.

  Test MicroF1 score:
  >>> '%.2f' % getMicroF1(4, 5, 1)
  '0.62'

  '''

  precision = tp / (tp + fp)
  accuracy = tp / (tp + fn)

  f1 = (precision + accuracy) / 2
  return f1

def getMacroF1(scores):
  """
  Test MacroF1:
  >>> '%.2f' % getMacroF1([0.6, 0.7])
  '0.65'
  """
  return sum(scores) / len(scores)


def main():
  #G = nx.read_edgelist("data\class_data\CA-GrQc.txt", nodetype=int)
  #save_graph(G, "plot.png")
  X = int(input("input number for Distance: "))
  if X < 3:
    print('Distance must be at least 3.\nExiting...')
    return

  with open("data\class_data\CA-GrQc.txt", 'r') as f:
    lines = f.read().splitlines()
  lines = [list(map(int, line.split())) for line in lines]

  #Runs Union-find algorithm
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

  false_negatives = len(not_in_cluster_with3)
  true_positives = len(more)
  false_positives = len(hasX) - true_positives
  microF1_inside = getMicroF1(true_positives, false_positives, false_negatives)


  false_negatives = len(members) - len(more)
  true_positives = len(not_in_cluster) - len(not_in_cluster_with3)
  false_positives = len(not_in_cluster_with3)
  microF1_outside = getMicroF1(true_positives, false_positives, false_negatives)

  macroF1 = getMacroF1([microF1_inside, microF1_outside])



  print(f"Not in cluster (Negative Coverage): {len(not_in_cluster)}")
  print(f"Not in cluster with {X} neighbors (Incorrect Negative Classifications): {len(not_in_cluster_with3)}")
  print(f"Ratio (negatives that trigger the rule): {len(not_in_cluster_with3)*100/len(not_in_cluster):.3f} %")
  print(f"Ratio (negative accuracy): {100 - len(not_in_cluster_with3)*100/len(not_in_cluster):.3f} %")
  print(f"Has {X} neighbors (Positive Coverage): {len(hasX)}")
  print(f"Has {X} neighbors and is in large cluster (Positive Classifications): {len(more)}")
  print(f"In large cluster: {len(members)}")
  print(f"Ratio: {len(more)*100/len(members):.3f} %")
  print(f'\nMicro F1 Score (Inside inner circle): {microF1_inside :.3f}')
  print(f'Micro F1 Score (Outside inner circle): {microF1_outside :.3f}')
  print(f'Macro F1 Score: {macroF1 :.3f}')

    
if __name__ == '__main__':
  import timeit
  main()
  #print(timeit.timeit("main()"))
