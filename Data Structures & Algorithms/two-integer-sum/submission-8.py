from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       new_map = {}
       for i in range (len(nums)):
        difference = target - nums[i]
        if difference in new_map:
            return [new_map[difference], i]
        new_map[nums[i]] = i
      
    

        
        
            
