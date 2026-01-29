Num_Tests = int(input())  # number of test cases

for i in range(Num_Tests):
    F = int(input())      # number of friendships
    parent = {}           # parent[x] = representative of x's network
    size = {}             # size[root] = size of that network

    def find(x):
        # find root of x with path compression
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        # merge networks of a and b, r means root
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[rb] = ra           # attach rb under ra
            size[ra] += size[rb]      # update network size
        return size[find(a)]          # return merged network size

    for _ in range(F):
        a, b = input().split()        # friendship pair

        # initialize new people
        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1

        print(union(a, b))            # output network size
