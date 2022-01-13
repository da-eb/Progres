nums = [3,2,4]
target = 6

class Solution:

    def __init__(self):
        self.nums = nums
        self.target = target
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # index = f"{fir}{sec}"
        # index =[]
        for i in nums:
            fir = (len(nums) - len(nums))
            sec = (len(nums) + 1) - len(nums)
            if fir + sec != target:
                sec += 1
                if fir + sec != target:
                    fir += 1