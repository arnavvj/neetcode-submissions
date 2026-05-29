class Solution:

    def encode(self, strs: List[str]) -> str:

        ans = ""

        for word in strs:
            ans += word + "\\#\\#"

        return ans

    def decode(self, s: str) -> List[str]:

        if len(s) == 0:
            return []

        ans = s.split("\\#\\#")

        return ans[:-1]




