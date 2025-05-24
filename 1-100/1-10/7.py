class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x=abs(x)
        s=0
        while x!=0:
            s=s*10+x%10
            x//=10
        s*=sign

        if s<-2**31 or s>2**31-1:
            return 0
        return s