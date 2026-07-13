from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_map = defaultdict(list)
        complement = 0
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in array_map.keys():
                return [array_map[complement], i]
            array_map[nums[i]] = i
    

      
    

        
        
            
