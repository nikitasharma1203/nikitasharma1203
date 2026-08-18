class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashnet = set()
        for i in range(len(nums)):
            if nums[i] in hashnet:
                return True
            else:
                hashnet.add(nums[i])
        return False

