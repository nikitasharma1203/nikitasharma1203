class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        seen = Counter(nums)
        max_freq = max(seen.values())
        return sum(v for v in seen.values() if v == max_freq)