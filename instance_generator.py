import random

def edgesCreator(x, y, dens):
  selected = []
  quantity = int((x * y)* (dens/100))
  edges = []
  
  for a in range(1, x + 1) :
    for b in range(1, y + 1) :
      edges.append((("c" + str(a)), ("v" + str(b))))

  for i in range(quantity):
    a,b  = random.choice(edges)
    
    selected.append((a,b))
    edges.remove((a,b))

  return selected