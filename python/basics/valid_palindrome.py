'''A phrase is a palindrome if, after converting all 
uppercase letters into lowercase letters and removing all non-alphanumeric 
characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s)-1

        while i<=j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i].lower()!=s[j].lower():
                return False
            j-=1;i+=1
        return True
            