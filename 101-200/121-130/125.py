class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a="qwertyuioplkjhgfdsazxcvbnm0123456789"
        b=""
        for i in s:
            if i in a:
                b = b+i
        
        if len(b)==0:
            return True

        c = b[::-1]
        if c==b:
            return True
        else:
            return False


