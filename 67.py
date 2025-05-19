class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l= max(len(a), len(b))
        a=a.zfill(l)
        b=b.zfill(l)

        carry= 0
        result = []

        for i in range(l-1,-1,-1):
            bita=int(a[i])
            bitb=int(b[i])

            t = bita + bitb + carry
            carry = t//2
            result.append(str(t%2))

        if carry:
            result.append("1")