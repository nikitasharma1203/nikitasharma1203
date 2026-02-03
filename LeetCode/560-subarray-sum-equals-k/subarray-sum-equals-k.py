from collections import defaultdict



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        prefix_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1   # base case: sum=0 occurs once

        for num in nums:
            prefix_sum += num
            # check if there was a prefix_sum that makes current_sum - k
            if (prefix_sum - k) in prefix_counts:
                count += prefix_counts[prefix_sum - k]
            # record this prefix_sum
            prefix_counts[prefix_sum] += 1

        return count

