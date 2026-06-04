class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        ans = [float('inf')] * (amount + 1)
        ans[0] = 0

        for c in coins:
            for i in range(1, amount + 1):

                c_ = float('inf')
                if i % c == 0:
                    c_ = i // c

                if i >= c:

                    ans[i] = min(
                        ans[i],       # preserve previous best
                        c_,
                        ans[i-c] + 1
                    )

            print(ans)

        return ans[-1] if ans[-1] != float('inf') else -1