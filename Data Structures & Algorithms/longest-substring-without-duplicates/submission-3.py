class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        limit = len(s)

        if limit == 1 or limit == 0:
            return limit
        
        ans = float('-inf')
        
        cset = set()
        i, j = 0, 1
        cset.add(s[i])

        while(i < limit and j < limit):
            
            if s[j] not in cset:
                cset.add(s[j])
                j += 1

            else:
                ans = max(ans, j - i)
                cset= set()
                i += 1
                cset.add(s[i])
                j = i + 1
        
        ans = max(ans, j - i)

        return ans



"""

  0 1 2 3 4 5 6
" z x y z x y z "
        i
          j 

  dict{
  
  }  

"""