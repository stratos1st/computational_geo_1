import ast

def CCW(p1,p2,p3):
  if (p3[1]-p1[1])*(p2[0]-p1[0]) > (p2[1]-p1[1])*(p3[0]-p1[0]):
    return True
  return False

def GiftWrapping(Points):
  last_hull_point=min(a)
  Hull=[]
  while True:
    Hull.append(last_hull_point)
    point_checking=Points[0]
    n = len(Points)
    for j in range(1,n):
      if point_checking==last_hull_point or not CCW(Points[j],Hull[-1],point_checking):
        point_checking = Points[j]
    last_hull_point = point_checking
    if last_hull_point in Points:
      Points.remove(last_hull_point)
    if point_checking == Hull[0]:
      break
  return Hull

a = ast.literal_eval(input('points: '))
h=GiftWrapping(a)
for x in range(len(h)): 
    print(h[x])

#[(-2,1),(0,0),(1,1),(1,-1)] ok
#[(-2,1),(0,0),(1,1),(2,2)] ok
#[(-2,1),(0,0),(2,2),(1,1)] fail