class Solution(object):
    def isPalindrome(self, s):
        
        s = s.lower()
        pattern = r'[^A-Za-z0-9]+'
        s = re.sub(pattern, '', s)
        if len(s) == 1 or len(s) == 0:
            return True
        j = (len(s)-1)
        for i, x in enumerate(s):
            if i >=  j:
                return True
            if x != s[j]:
                return False
            j -= 1
            
        