class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        counts = list(freq.values())
        return len(set(counts)) == len(counts)