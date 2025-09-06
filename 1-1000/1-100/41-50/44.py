class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp = -1
        
        while s_idx < s_len:
            # Single character match
            if p_idx < p_len and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
                s_idx += 1
                p_idx += 1
            # Found '*', save position for potential backtrack
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp = s_idx
                p_idx += 1
            # No match, but we have a '*' to fall back to
            elif star_idx != -1:
                p_idx = star_idx + 1
                s_tmp += 1
                s_idx = s_tmp
            else:
                return False
        
        # Check remaining pattern contains only '*'
        return all(p[i] == '*' for i in range(p_idx, p_len))