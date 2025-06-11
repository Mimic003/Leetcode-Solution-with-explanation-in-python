class Solution:
    def climbStairs(self, n: int) -> int:
        ps, cs = 0,1
        for  _ in range(n):
            ps, cs = cs, ps+cs  
        return cs