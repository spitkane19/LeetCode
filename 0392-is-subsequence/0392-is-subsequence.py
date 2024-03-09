class Solution(object):
    def isSubsequence(self, s, t):
        if s == "":
            return True
        c=0
        for letter in t:
            if letter == s[c]:
                c += 1
                if c == len(s):
                    return True
        return False
            
        