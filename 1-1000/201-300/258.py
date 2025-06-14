class Solution:
    def addDigits(self, num: int) -> int:
        if num < 0:
            num = -num
        if num < 10:
            return num
        while num > 9:
            num = self.ad(num)
        return num

    def ad(self, n):
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s