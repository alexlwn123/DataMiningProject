import pandas as pd
from scipy.signal import convolve2d
def main():
  data = pd.read_csv("data\CA-GrQc.txt", sep="\t")
   # com-dblp.ungraph.txt
  print(data)


if __name__ == '__main__':
  main()
