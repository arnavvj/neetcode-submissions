class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        map_ = {}

        for n in nums:

            try:

                if map_[n] == 1:
                    return True
            
            except KeyError:

                map_[n] = 1

            print(map_)

        return False

        