from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        count = 0
        
        for x in nums:
            target = k - x
            if freq[target] > 0:
                freq[target] -= 1
                count += 1
            else:
                freq[x] += 1
        
        return count
