import random
class BipartiteGraph :
  def __init__(self, edges) :
    self.edges = edges
    self.adj_list = {}

    for u, v in edges :
      if u not in self.adj_list :
        self.adj_list[u] = []
      if v not in self.adj_list :
        self.adj_list[v] = []
      self.adj_list[u].append(v)
      self.adj_list[v].append(u)

    self.matching = {}
    self.dist = {}
    self.parent = {}

  def path_to_root(self, v) :
    i = v
    path = [i]
    while self.parent[i] :
      i = self.parent[i]
      path.append(i)
    return path

  def root(self, v) :
    path = self.path_to_root(v)
    return path[-1]

  def find_augmenting_path(self) :
    F = []

    #iniciar arvores em F
    for v in self.adj_list :
      if v not in self.matching :
        self.parent[v] = None
        self.dist[v] = 0
        F.append(v)

    marked_vertices = []
    marked_edges = []

    #marcar arestas do matching
    for u, v in self.matching.items() :
      marked_edges.append((u, v))
      marked_edges.append((v, u))

    #enquanto tem vertice não marcado dist par da raiz
    for v in F:
      if v not in marked_vertices and self.dist[v] % 2 == 0 :

        #enquanto existir aresta não marcada (v, w)
        for w in self.adj_list[v] :
          if (v, w) not in marked_edges:

            if w not in F :
              #então w não é vértice simples
              x = self.matching[w]
              #add (v, w) e (w, x) à árvore de v
              self.parent[w] = v
              self.parent[x] = w
              self.dist[w] = self.dist[v] + 1
              self.dist[x] = self.dist[w] + 1
              F.append(w)
              F.append(x)
            else :
              if self.dist[w] % 2 != 0 :
                continue
              if self.root(v) != self.root(w) :
                P1 = self.path_to_root(v)
                P2 = self.path_to_root(w)
                P = P1[::-1] + P2
                return P

          marked_edges.append((v, w))
      marked_vertices.append(v)

    return []

  def max_matching(self) :
    while True :
      path = self.find_augmenting_path()
      if not path :
        break
      self.switch_path(path)

    return len(self.matching) // 2

  def switch_path(self, path) :
    for i in range(0, len(path) - 1, 2):
            u = path[i]
            v = path[i + 1]
            # Alterna o emparelhamento
            self.matching[u] = v
            self.matching[v] = u

def readFile(file):
  params = []
  temp = open(file)
  line = temp.readline()
  while line:
    params.append(int(line))
    line = temp.readline()
  return params

def edgesCreator(x, y, dens):
  selected = []
  quantity = int((x * y)* (dens/100))
  edges = [(a,b) for a in range(x) for b in range(y)]
  
  for i in range(quantity):
    a,b  = random.choice(edges)
    print("a,b: ",(a,b))
    print("b,a: ",(b,a))  
    
    selected.append((a,b))
    edges.remove((a,b))

  return selected

# Exemplo de uso:
entrada = readFile("entrada.txt")
print(edgesCreator(entrada[0],entrada[1],entrada[2]))

# Exemplo de uso:
#edges = [(1, 8), (1, 9), (3, 7), (3, 10), (4, 9), (5, 9), (5, 10), (6, 12)]
#graph = BipartiteGraph(edges)
#max_matching = graph.max_matching()
#print("O tamanho do emparelhamento máximo é:", max_matching)
#print("Emparelhamentos:", graph.matching)