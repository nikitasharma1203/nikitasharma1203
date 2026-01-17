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
"""
brute force(o(n^2))
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
"""