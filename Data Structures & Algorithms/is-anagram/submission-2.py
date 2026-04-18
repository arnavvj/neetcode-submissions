class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_len = len(s)
        if s_len != len(t):
            return False

        s_dict, t_dict = dict(), dict()
        for i in range(0, s_len):

            try:
                s_dict[s[i]] += 1
            except KeyError:
                s_dict[s[i]] = 1        

            try:
                t_dict[t[i]] += 1
            except KeyError:
                t_dict[t[i]] = 1

        for (ks,vs) in s_dict.items():
            try:
                if vs != t_dict[ks]:
                    return False
            except KeyError:
                return False 

        return True