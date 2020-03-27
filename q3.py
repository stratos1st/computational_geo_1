# Implement the incremental 2D algorithm for computing the convex hull of a
# finite set of points in the plane.

# http://geomalgorithms.com/a12-_hull-3.html
# http://www.ams.sunysb.edu/~jsbm/courses/345/13/melkman.pdf
# https://docs.python.org/2/library/collections.html#collections.deque
# https://wiki.python.org/moin/TimeComplexity

from collections import deque
import numpy as np


# returns ccw
def ccw(A: np.array, B: np.array, C: np.array) -> int:
    # Tests whether the turn formed by A, B, and C is ccw
    return (B['x'] - A['x']) * (C['y'] - A['y']) - (B['y'] - A['y']) * (C['x'] - A['x'])


# returns the last n elements (without removing them)
def look(que: deque, n: int) -> np.array:
    if n <= 0:
        return np.empty(shape=(0, 0))
    ans=np.empty(shape=(n), dtype=[('x', float), ('y', float)])
    for i in range(0,n):
        ans[i]=que.pop()
    for i in range(n-1,-1,-1):
        que.append(ans[i])
    return ans


# returns the first n elements (without removing them)
def lookLeft(que: deque, n: int) -> np.array:
    if n <= 0:
        return np.empty(shape=(0, 0))
    ans=np.empty(shape=(n), dtype=[('x', float), ('y', float)])
    for i in range(0,n):
        ans[i]=que.popleft()
    for i in range(n-1,-1,-1):
        que.appendleft(ans[i])
    return ans


def convexHull2d(points_input: np.array) -> np.array:
    # sort points declining
    points=np.sort(points_input, kind='mergesort', order=['x','y'])

    # find the last non collinear point to the first two
    last_non_inline=2
    while ccw(points[0], points[1],points[last_non_inline]) == 0:
        last_non_inline += 1
        if last_non_inline == len(points):
            return np.empty(len(points), dtype=[('x', float), ('y', float)])

    # initialise deque with
    if ccw(points[0], points[last_non_inline-1], points[last_non_inline]) > 0:
        que = deque([points[last_non_inline], points[0], points[last_non_inline-1], points[last_non_inline]])
    elif ccw(points[0], points[last_non_inline-1], points[last_non_inline]) < 0 :
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

        # remove all bottom points inside our (soon to be) polygon
        bot = look(que, 2)
        while ccw(bot[1], bot[0],points[i]) <= 0:
            que.pop()
            bot = look(que,2)
        que.append(points[i])

        # remove all top points inside our (soon to be) polygon
        top = lookLeft(que, 2)
        while ccw(top[0], top[1], points[i]) <= 0:
            que.popleft()
            top = lookLeft(que,2)
        que.appendleft(points[i])

    # reform output (not really needed)
    ans=np.empty(shape=(que.__len__()-1), dtype=[('x', float), ('y', float)])
    for i in range(0,que.__len__()-1):
        ans[i]=que.pop()
    return ans

# -------------------------------------main----------------------

# inputt=[(0,0),(1,1),(-1,1),(1,-1),(-1,-1)]

# inputt=[(0, 2), (2, 2), (4, 2), (3, 3),
#       (3, 2), (3, 1), (5, 2), (0, 2),
#       (2, 4), (2, 0), (4, 4), (6, 2), (4, 0)]


inputt=[(0, 1),(0, 3),(0, 2), (2, 2), (4, 2), (3, 3),
      (3, 2), (3, 1), (5, 2), (0, 2),
      (2, 4), (2, 0), (4, 4), (6, 2), (4, 0)]

input = np.array(inputt, dtype=[('x', float), ('y', float)])
ans=convexHull2d(input)
for i in ans:
    print(i)
