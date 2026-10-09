from collections import deque

n = int(input())
items = []
for _ in range(n):
    items.append(input())

m = int(input())

graph = { }

for item in items:
    graph[item] = []

for _ in range(m):
    a, b = input().split()
    graph[a].append(b)
    graph[b].append(a)

color = {}

for item in items:
    color[item] = -1
possible = True

for start in items:
    if color[start] != -1:
        continue

    color[start] = 0
    q = deque([start])

    while q:
        current = q.popleft()
        for neighbour in graph[current]:
            if color[neighbour] == -1:
                color[neighbour] = 1 - color[current]
                q.append(neighbour)

            elif color[neighbour] == color[current]:
                possible = False
                break

        if not possible:
            break
    if not possible:
        break

if not possible:
    print('impossible')
else:
    walter = []
    jesse = []

    for item in items:
        if color[item] == 0:
            walter.append(item)
        else:
            jesse.append(item)
    print(" ".join(walter))
    print(" ".join(jesse))
