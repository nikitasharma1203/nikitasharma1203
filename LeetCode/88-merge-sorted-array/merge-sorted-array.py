class Solution:
    def merge(self, nums1, m, nums2, n):
        # Copy nums2 into the empty slots of nums1
        nums1[m:] = nums2
        # Sort the combined array
        nums1.sort()
