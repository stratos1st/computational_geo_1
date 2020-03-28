# Implement the incremental 2D algorithm for computing the convex hull of a
# finite set of points in the plane.

# http://geomalgorithms.com/a12-_hull-3.html
# http://www.ams.sunysb.edu/~jsbm/courses/345/13/melkman.pdf
# https://docs.python.org/2/library/collections.html#collections.deque
# https://wiki.python.org/moin/TimeComplexity

from collections import deque
import numpy as np
import sys


# returns ccw
def ccw(A: np.array, B: np.array, C: np.array) -> float:
    # Tests whether the turn formed by A, B, and C is ccw
    return (B['x'] - A['x']) * (C['y'] - A['y']) - (B['y'] - A['y']) * (C['x'] - A['x'])


def convexHull2d(points_input: np.array) -> np.array:
    # sort points declining
    points=np.sort(points_input, kind='mergesort', order=['x','y'])

    # find the last non collinear point to the first two
    last_non_inline=2
    while ccw(points[0], points[1],points[last_non_inline]) == 0:
        last_non_inline += 1
        if last_non_inline == len(points):
            return np.empty(shape=(0, 0))

    # initialise deque with
    if ccw(points[0], points[last_non_inline-1], points[last_non_inline]) > 0:
        que = deque([points[last_non_inline], points[0], points[last_non_inline-1], points[last_non_inline]])
    elif ccw(points[0], points[last_non_inline-1], points[last_non_inline]) < 0:
        que = deque([points[last_non_inline], points[last_non_inline-1], points[0], points[last_non_inline]])
    else:
        print("error")
        return []

    for i in range(last_non_inline, len(points)):
        # maybe we dont need this
        # bot = look(que, 2)
        # top = lookLeft(que, 2)
        # if(ccw(top[0], top[1],points[i]) > 0 and
        #    ccw(bot[1], bot[0],points[i]) > 0):
        #     continue

        # remove all bottom points inside o (soon to be) polygon
        while ccw(que[-2], que[-1], points[i]) <= 0:
            que.pop()
        que.append(points[i])

        # remove all top points inside our (soon to be) polygon
        while ccw(que[0], que[1], points[i]) <= 0:
            que.popleft()
        que.appendleft(points[i])

    # reform output (not really needed)
    ans=np.empty(shape=(que.__len__()-1), dtype=[('x', float), ('y', float)])
    for i in range(0,que.__len__()-1):
        ans[i]=que.pop()
    return ans

# -------------------------------------main----------------------

# read from file
file_name = sys.stdin.readline()
inputt = []
with open(file_name[:-1]) as myfile:
    for line in myfile:
        x, y = line.partition(" ")[::2]
        inputt.append((float(x), float(y)))

input = np.array(inputt, dtype=[('x', float), ('y', float)])
ans=convexHull2d(input)
for i in ans:
    print(i)

