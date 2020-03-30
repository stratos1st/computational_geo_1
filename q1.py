import ast

def CCW(p1,p2,p3):
  return (p3[1]-p1[1])*(p2[0]-p1[0])-(p2[1]-p1[1])*(p3[0]-p1[0])


points = ast.literal_eval(input('points: '))
if(CCW(points[0],points[1],points[2]) == 0):
  print("points are collinear there is no tringle")

rot1 = CCW(points[0],points[1],(0,0))
rot2 = CCW(points[1],points[2],(0,0))
rot3 = CCW(points[2],points[0],(0,0))

if(rot1*rot2 >= 0 and rot2*rot3 >=0):
  print("zero is inside the tringle")
else:
  print("zero is outside of the tringle")

#---------inside--------
#[(1,1),(-1,1),(0,-1)] ok 
#[(1,1),(0,-1),(-1,1)] ok
#[(0,-1),(-1,1),(1,1)] ok 
#--------bearly_in------
#[(1,1),(-1,1),(-1,-1)] ok
#---------outside-------
#[(1,1),(-1,1),(-1.1,-1)] ok