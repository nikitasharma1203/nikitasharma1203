class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        max_num = nums[0]
        for i in nums[1:]:
            current = max(i, current + i)
            max_num = max(current, max_num)
        return max_num