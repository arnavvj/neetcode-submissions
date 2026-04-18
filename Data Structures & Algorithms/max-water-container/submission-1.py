class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        i, j = 0, len(heights) - 1

        while (i<j):
            ans = max(
                ans, 
                min(heights[i], heights[j]) * (j-i)
            )

            if heights[i] <= heights[j]:
                i+=1
            else:
                j-=1

        return ans
        

"""
  0   1   2   3   4   5   6   7
[ 1 , 7 , 2 , 5 , 4 , 7 , 3 , 6 ]
      i
                              j

"""