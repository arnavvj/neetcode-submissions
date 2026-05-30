class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ans = 0

        for i in range (0, len(s)):
            
            # single or self char substring
            ans += 1

            # expanding window for odd palindrome
            j, k = i-1, i+1
            while (j >= 0 and k < len(s)):
                if s[j] == s[k]:
                    ans += 1
                else:
                    break
                j -= 1
                k += 1

            # expanding window for even palindrome
            j, k = i, i+1
            while (j >= 0 and k < len(s)):
                if s[j] == s[k]:
                    ans += 1
                else:
                    break
                j -= 1
                k += 1

        return ans