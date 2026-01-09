from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        operations = 0 
        for num in nums:
            partner = k - num
            if count.get(partner,0) > 0:
                operations +=1
                count[partner] -=1
            else:
                count[num] = count.get(num,0) +1
        return operations