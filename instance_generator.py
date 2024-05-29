import random

def edgesCreator(x, y, dens):
  selected = []
  quantity = int((int(x) * int(y))* (int(dens)/100))
  edges = []
  
  for a in range(1, int(x) + 1) :
    for b in range(1, int(y) + 1) :
      edges.append((("c" + str(a)), ("v" + str(b))))

  for i in range(quantity):
    a,b  = random.choice(edges)
    
    selected.append((a,b))
    edges.remove((a,b))

  return selected

def instanceCreator(edges):
  with open("instance.txt", "w") as file:
    for i in edges:
      line = f'{i}\n'
      file.write(line)


quantC = input("Digite a quantidade de Candidatos: ")
quantV = input("Digite a quantidade de Vagas: ")
dens = input("Digite a Densidade do grafo (sem '%'): ")
edges = edgesCreator(quantC, quantV, dens)
instanceCreator(edges)