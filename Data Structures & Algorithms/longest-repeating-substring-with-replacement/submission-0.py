class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        ans = 1

        for i in range(len(s)-1):

            # new start and new check
            cmap = {}
            cmap[s[i]] = 1
            max_occ_char = s[i]

            for j in range(i+1, len(s)):

                # update char map and count
                count = cmap.get(s[j], 0) + 1
                cmap[s[j]] = count
                
                # update max occuring char based on count
                if cmap[s[j]] > cmap[max_occ_char]:
                    max_occ_char = s[j]

                # if (min occuring chars = len of window - max occuring chars) <= k
                # then replacement possible and update ans
                # else continue search
                if (j+1 - i - cmap[max_occ_char]) <= k:
                    ans = max(ans, j+1-i)

        return ans