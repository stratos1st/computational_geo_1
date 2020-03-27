# Given a circle of radius r in the plane with (0, 0) as center, implement an
# algorithm that finds the total lattice points on the circumference.
# Lattice Points are points
# with integer coordinates.

import math

# count Lattice points
def countLatticePoints(r):
    if r <= 0:  # error
        return 0
    result=0
    # Check every int value
    for x in range(1, int(r)+1):  # range inclusive, r rounded down
        y = math.sqrt(r*r-x*x)  # Find potential y
        if y.is_integer():
            result += 4  # one for each quadrant
    return result


# ----------------main--------------------
r=float(input("enter r for ((0,0),r) circle: "))
print("total lattice points: "+str(countLatticePoints(r)))

