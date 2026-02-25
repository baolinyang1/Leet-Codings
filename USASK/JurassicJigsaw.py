# Compute Hamming distance between two DNA strings
# (number of positions where the characters differ)
def hamming(a: str, b: str) -> int:
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
    return cnt


def main():
    # Read n = number of samples
    # Read k = length of each DNA string
    n, k = map(int, input().split())

    # Read all DNA samples
    dna = [input().strip() for _ in range(n)]

    # We will build a Minimum Spanning Tree (MST)
    # using Prim's algorithm.

    INF = 10**9  # A very large number

    # in_mst[i] = True if node i is already in the MST
    in_mst = [False] * n

    # dist[i] = smallest edge weight connecting node i
    #           to the current MST
    dist = [INF] * n

    # parent[i] = the node that connects i to the MST
    parent = [-1] * n

    # Start Prim’s algorithm from node 0
    # Distance to itself is 0 (so it gets picked first)
    dist[0] = 0

    total = 0  # This will store total MST weight

    # We need to add exactly n nodes into MST
    for _ in range(n):

        # Step 1: Pick the node u not yet in MST
        # with the smallest dist[u]
        u = -1
        best = INF
        for i in range(n):
            if not in_mst[i] and dist[i] < best:
                best = dist[i]
                u = i

        # Add u to MST
        in_mst[u] = True

        # Add its edge weight to total
        total += dist[u]

        # Step 2: Update distances of remaining nodes
        # Check all other nodes v not yet in MST
        for v in range(n):
            if not in_mst[v]:

                # Compute Hamming distance (edge weight)
                w = hamming(dna[u], dna[v])

                # If this edge is better (smaller weight),
                # update dist[v] and parent[v]
                if w < dist[v]:
                    dist[v] = w
                    parent[v] = u

    # Print minimal total unlikeliness (MST weight)
    print(total)

    # Print the edges of the MST
    # For each node except root (0),
    # print parent and node index
    for v in range(1, n):
        print(parent[v], v)


if __name__ == "__main__":
    main()