class Solution:
    def numDecodings(self, s: str) -> int:
        # preprocess
        n = len(s)
        prev_prev,prev,curr = 1,1,1
        # dp
        for i in range(1,n+1):
            if s[i-1] == '0':
                if i == 1 or s[i-2] not in {"1","2"}:
                    return 0
                curr = prev_prev
            elif i>1 and 10 < int(s[i-2:i]) <= 26:
                curr = prev + prev_prev
            else:
                curr = prev
            prev, prev_prev = curr, prev