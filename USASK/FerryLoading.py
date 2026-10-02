# this one uses DP!!!
def ferry_loading(L_meters, cars):
    L = L_meters * 100
    #How many centimeters of the PORT side are currently occupied.
    dp = [False] * (L + 1)
    dp[0] = True # After loading all cars processed so far, there exists some valid arrangement where port has exactly p cm occupied
    parents = []
    prefix = 0 # prefix = total length of all cars loaded so far. so total cars = port + starboard
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

        


# def ferry_loading(L_meters, cars):
#     L = L_meters * 100
#     n = len(cars)

#     # prefix[i] = total length of first i cars
#     prefix = [0] * (n + 1)

#     for i in range(1, n + 1):
#         prefix[i] = prefix[i - 1] + cars[i - 1]

#     # dp[i][p] = True if first i cars can be loaded
#     # with p cm used on port
#     dp = [[False] * (L + 1) for _ in range(n + 1)]

#     dp[0][0] = True

#     loaded = 0

#     for i in range(n):
#         car = cars[i]

#         for p in range(L + 1):

#             if not dp[i][p]:
#                 continue

#             # OPTION 1: Put current car on PORT
#             if p + car <= L:
#                 dp[i + 1][p + car] = True

#             # OPTION 2: Put current car on STARBOARD
#             starboard = prefix[i] - p

#             if starboard + car <= L:
#                 dp[i + 1][p] = True

#         # Check if this car could be loaded at all
#         if not any(dp[i + 1]):
#             break

#         loaded = i + 1

#     # Find any valid final port length
#     p = dp[loaded].index(True)

#     result = []

#     # Work backwards
#     for i in range(loaded, 0, -1):
#         car = cars[i - 1]

#         # Could we have arrived here by putting car on starboard?
#         if dp[i - 1][p] and prefix[i - 1] - p + car <= L:
#             result.append("starboard")

#         else:
#             # Then it must have gone on port
#             result.append("port")
#             p -= car

#     result.reverse()

#     return loaded, result


# def main():
#     L = int(input())

#     cars = []

#     while True:
#         car = int(input())

#         if car == 0:
#             break

#         cars.append(car)

#     loaded, result = ferry_loading(L, cars)

#     print(loaded)

#     for side in result:
#         print(side)


# if __name__ == "__main__":
#     main()