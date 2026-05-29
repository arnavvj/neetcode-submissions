class Solution:

    def encode(self, strs: List[str]) -> str:

        ans = ""

        for word in strs:
            ans += word + "#wekvj#"

        return ans

    def decode(self, s: str) -> List[str]:

        if len(s) == 0:
            return []

        ans = s.split("#wekvj#")

        return ans[:-1]




