class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}

        def dfs(n):

            if n in cache:
                return cache[n]
            
            if n == 0:
                return 1
            
            if n < 0:
                return 0
            
            cache[n] = dfs(n - 1) + dfs(n - 2)
            return cache[n]
        
        return dfs(n)

        


        

        