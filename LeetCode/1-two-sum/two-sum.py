"""hashmap(o(n))"""
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, j in enumerate(nums):
            complement = target - j
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[j] = i