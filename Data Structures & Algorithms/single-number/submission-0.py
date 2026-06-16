class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = 0
        for num in nums:
            if nums.count(num) ==1:
                once = num
        return once

        