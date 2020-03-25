# Time:O（n）Space:O（n），
# 只用遍历一遍列表，因为字典内的查找是常量操作，所以是O(n)
# 每次查找字典并记录，直到全部num记录
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}
        for index, value in enumerate(nums):
            if target - value in data:
                return data[target-value] , index
            data[value] = index
            
            
    #O(n^2) O（1）
    #     ls = len(nums)
    #     for i in range(ls):
    #         for j in range(i + 1, ls):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]