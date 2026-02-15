# # YOU CAN USE THIS, BUT THIS IS WAY TOO SLOW!
# import math
# shots = int(input())

# # i want a function that takes a list of tuples and calculate the max dis and return
# def calculate(arr):
#     max = 0
#     for i in range(len(arr)):
#         for j in range(1,len(arr)):
#             if arr[i] != arr[j]:
#                 res = math.sqrt((arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2)
#                 if res > max:
#                     max = res

#     return max

# dis = []
# for i in range(shots):
#     tmpt = list(map(int, input().split()))
#     dis.append(tmpt)

# print(calculate(dis))

import math

def cross(o, a, b):
    """2D cross product (OA x OB). Positive if o->a->b makes a left turn."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    """
    Returns the convex hull of a set of 2D points (as a list of points),
    in counterclockwise order, without repeating the first point at the end.
    Monotonic chain: O(n log n).
    """
    points = sorted(set(points))  # sort and remove duplicates
    n = len(points)
    if n <= 1:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # last point of each list is the starting point of the other list
    return lower[:-1] + upper[:-1]

def dist2(a, b):
    """Squared distance (avoid sqrt until the end)."""
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy

def diameter_of_convex_polygon(poly):
    """
    Rotating calipers to find maximum distance on a convex polygon.
    poly is CCW order, no repeated end point.
    Returns max squared distance.
    """
    m = len(poly)
    if m == 0:
        return 0
    if m == 1:
        return 0
    if m == 2:
        return dist2(poly[0], poly[1])

    j = 1
    best = 0

    # For each edge i -> i+1, move j while area increases
    for i in range(m):
        ni = (i + 1) % m

        # Move j as long as the parallelogram area increases
        while True:
            nj = (j + 1) % m
            cur = abs(cross(poly[i], poly[ni], poly[j]))
            nxt = abs(cross(poly[i], poly[ni], poly[nj]))
            if nxt > cur:
                j = nj
            else:
                break

        # Update best distances using current i and found j
        best = max(best, dist2(poly[i], poly[j]), dist2(poly[ni], poly[j]))

    return best

def main():
    C = int(input().strip())
    pts = []
    for _ in range(C):
        x, y = map(int, input().split())
        pts.append((x, y))

    hull = convex_hull(pts)
    best_sq = diameter_of_convex_polygon(hull)
    print(math.sqrt(best_sq))

if __name__ == "__main__":
    main()
