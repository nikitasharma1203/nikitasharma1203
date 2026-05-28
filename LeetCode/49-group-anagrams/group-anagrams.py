from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sort the word to get a canonical key
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())

"""write the time/space complexity and what pattern it used."""