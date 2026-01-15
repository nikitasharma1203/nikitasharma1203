from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Step 1: prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Step 2: suffix products
        suffix = 1
        for j in range(n-1, -1, -1):
            answer[j] *= suffix
            suffix *= nums[j]

        return answer
