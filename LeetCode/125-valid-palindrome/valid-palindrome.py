class Solution:
    def isPalindrome(self, s: str) -> bool:
        resplace_string_ele = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        return resplace_string_ele == resplace_string_ele[::-1]