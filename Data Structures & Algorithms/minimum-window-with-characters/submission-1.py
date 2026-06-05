class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_map = {}
        for c in t:
            try:
                t_map[c] += 1
            except KeyError:
                t_map[c] = 1

        ans = '0' * 1001
        import copy

        i = 0
        while(i<len(s)):
            if s[i] in t_map.keys():
                
                t_temp = copy.deepcopy(t_map)
                
                t_temp[s[i]] -= 1
                if t_temp[s[i]] == 0:
                    del(t_temp[s[i]])
                if not t_temp.keys():
                    if len(ans) > 1:
                        ans = s[i:i+1]
                        continue
                    
                j = i+1
                while (j < len(s)):

                    if s[j] in t_temp.keys():
                        
                        t_temp[s[j]] -= 1
                        if t_temp[s[j]] == 0:
                            del(t_temp[s[j]])  
                        if not t_temp.keys():
                            if len(ans) > j+1-i:
                                ans = s[i:j+1]
                                break
                    
                    j += 1

            i += 1

        return ans if len(ans) != 1001 else ""
        