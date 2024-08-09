import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.lower()
        
        for i,v in enumerate(s):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True