class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s)==1:
            return s
        
        st,e=0,0

        def eac(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return l+1,r-1

        for i in range(len(s)):
            l1,r1=eac(i,i)
            l2,r2=eac(i,i+1)

            if r1-l1>e-st:
                st,e=l1,r1
            if r2-l2>e-st:
                st,e=l2,r2
        
        return s[st:e+1]