class Solution(object):
    def isPalindrome(self, x):
        num = x
        rev = 0
        while x>0:
            d = x%10
            rev = rev*10+d
            x = x//10
        if rev == num:
            return True
        else:
            return False                