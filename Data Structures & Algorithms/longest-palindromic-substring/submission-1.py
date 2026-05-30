class Solution:
    def longestPalindrome(self, s: str) -> str:

        j = 0
        max_len = 1
        ans = s[0]

        while (j < len(s)):

            i, k = j-1, j+1
            while(i >= 0 and k < len(s)):
                if s[i] != s[k]:
                    break
                if k-i+1 > max_len:
                    max_len = k-i+1
                    ans = s[i:k+1]
                i -= 1
                k += 1
                
            i, k = j, j+1 
            while(i >= 0 and k < len(s)):
                if s[i] != s[k]:
                    break
                if k-i+1 > max_len:
                    max_len = k-i+1
                    ans = s[i:k+1]
                i -= 1
                k += 1
                        

            j += 1

        return ans

        


"""

a s d f g f d s e r g r e s d m m m f
^
                                    ^
"""