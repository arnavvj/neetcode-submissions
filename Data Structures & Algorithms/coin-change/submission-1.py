class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        ans = [float('inf')] * (amount + 1)
        ans[0] = 0

        for c in coins:
            for i in range(c, amount + 1):
                ans[i] = min(
                    ans[i],
                    ans[i - c] + 1
                )

            print(ans)

        return ans[-1] if ans[-1] != float('inf') else -1