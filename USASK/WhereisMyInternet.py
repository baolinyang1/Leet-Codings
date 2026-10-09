from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

q = deque([1])
visited[1] = True

while q:
    current = q.popleft()
    for neighbour in graph[current]:
        if not visited[neighbour]:
            visited[neighbour] = True
            q.append(neighbour)

not_connected = []

for i in range(1, n + 1):
    if not visited[i]:
        not_connected.append(i)

if not_connected:
    for house in not_connected:
        print(house)
else:
    print('Connected')