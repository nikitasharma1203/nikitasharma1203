from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tops = Counter(nums)
        return [num for num, _ in tops.most_common(k)]