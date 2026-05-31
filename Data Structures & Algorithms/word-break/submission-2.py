class Solution:

    def furtherBreak(self, s):

        ans = False

        if not s:
            return True

        if s in self.memo:
            return self.memo[s]

        for i in range(1, len(s)+1):

            if (s[:i] in self.wordDict):
                ans = ans or self.furtherBreak(s[i:])

                if ans:
                    self.memo[s] = True
                    return ans
        
        self.memo[s] = False
        return ans



    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        self.wordDict = wordDict
        self.memo = {}
        
        ans = False
        
        for i in range(1, len(s)+1):

            if (s[:i] in self.wordDict):
                ans = ans or self.furtherBreak(s[i:])

                if ans:
                    return ans

        return ans
        