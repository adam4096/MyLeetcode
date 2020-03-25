class Solution:
    def twoSum(self, nums: List[int], target: int):
           
        # hash 2
        hash_nums = {}
        for index, num in enumerate(nums):
            another = target - num
            try:
                hash_nums[another]
                return [hash_nums[another], index]
            except KeyError:
                hash_nums[num] = index