# class Solution:
#     def isUgly(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         while n%2==0 or n%3==0 or n%5==0:
#             if n%2==0:
#                 n/=2
#             elif n%3==0:
#                 n/=3
#             else:
#                 n/=5
#         if n==1:
#             return True
#         return False

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
           return False
        for prime in 2, 3, 5:
            while n % prime == 0:
                n //= prime
        return n == 1