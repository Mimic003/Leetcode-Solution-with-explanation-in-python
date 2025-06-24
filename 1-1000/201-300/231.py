class Solution(object):
    def isPowerOfTwo(self, n):
        if n<1:
            return False
        while n%2==0:
            n/=2
        
        return True if n==1 else False