class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels =set("aeiouAEIOU")
        v = [ch for ch in s if ch in vowels]
        return "".join(ch if ch not in vowels else v.pop() for ch in s)