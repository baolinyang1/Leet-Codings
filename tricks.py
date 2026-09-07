#boolean indexing:
import numpy as np

a = np.array([1,2,3,4,5])
mask = np.array([True, False, True, True, False])

print(a[mask])

#lru_cache cheat for noraml recursion:
#two things: u have to import first, then use @lru_cache(None) for the function that recures!
from functools import lru_cache
class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            return dfs(i, j+1) + dfs(i + 1, j)
        
        return dfs(0, 0)


#initalize 2d array:
memo = [[-1] * n for _ in range(m)]
#-> (m,n)!!!

#https://neetcode.io/problems/count-paths/solution, the last one is buffer trick, notice only the bottom and right gots them! 
#top-down DP == lru_cached recursion 
#buttom up: think baclwards, start from the end and go to the beginning

#In 2D DP, u can use either 2D array or just a dict {} with (i, j) as the key, but for dense ones: use array, irregular ones: use dict!
#like 2D grid uses array, but subsequence uses dict!