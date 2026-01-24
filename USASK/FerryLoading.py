# this one uses DP!!!
def ferry_loading(L_meters, cars):
    L = L_meters * 100
    dp = [False] * (L + 1)
    dp[0] = True
    parents = []
    prefix = 0
    loaded = 0
    for i, c in enumerate(cars):
        prefix += c
        new_dp = [False] * (L+1)
        parent = {} # CREATE A NEW DICT

        for p in range(L+1):
            if not dp[p]:
                continue
            # put on port
            if p + c <= L and prefix - (p+c) <=L:
                if not new_dp[p+c]:
                    new_dp[p + c] = True
                    parent[p + c] = (p, "port")
            #put on starboard
            if prefix - p <= L:
                if not new_dp[p]:
                    new_dp[p] = True
                    parent[p] = (p, "starboard")
        if not any(new_dp):
            break
        #Each parent dictionary stores all possible ways to reach every valid DP state after one car, which is why it contains many key–value pairs.     
        dp = new_dp
        parents.append(parent)
        loaded += 1

    if loaded == 0:
        return 0, []
    p = dp.index(True)
    result = []

    for i in range(loaded - 1, -1, -1):
        p, side = parents[i][p]
        result.append(side)
    
    result.reverse()
    return loaded, result


def main():
    L = int(input())
    cars = []

    while True:
        x = int(input())
        if x == 0:
            break
        cars.append(x)
    # CALL THE DP FUNCTION WITH LENGTH AND CARS ARRAY;
    k, ans = ferry_loading(L, cars)
    print(k)
    for s in ans:
        print(s)


if __name__ == "__main__":
    main()

                