from collections import defaultdict

#AL = defaultdict(list)
#print(AL[0])

import sys
from enum import Enum

class flag(Enum):
  UNVISITED = -1
  VISITED = -2

AL = []
status = []

def dfs(u):
  global AL
  global status

  sys.stdout.write(' '+str(u))
  status[u] = flag.VISITED.value
  for v, w in AL[u]:
    if status[v] == flag.UNVISITED.value:
      dfs(v)


def main():
  global AL
  global status

  fp = open('dfs_cc_in.txt', 'r')

  V = int(fp.readline().strip())
  AL = [[] for i in range(V)]
  for u in range(V):
    tkn = list(map(int, fp.readline().strip().split()))
    k = tkn[0]
    for i in range(k):
      v, w = tkn[2*i+1], tkn[2*i+2]
      AL[u].append((v, w))

  print('Standard DFS Demo (the input graph must be UNDIRECTED)')
  status = [flag.UNVISITED.value] * V
  numCC = 0
  for u in range(V):
    if status[u] == flag.UNVISITED.value:
      numCC += 1
      sys.stdout.write('CC %d:' % numCC)
      dfs(u)
      sys.stdout.write('\n')
  print('There are %d connected components' % numCC);


main()