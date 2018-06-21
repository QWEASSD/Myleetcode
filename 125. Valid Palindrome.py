
# coding: utf-8

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# Example: 2:
# Input: "race a car"
# Output: false
# 
# https://leetcode.com/problems/valid-palindrome/description/

# According to the question taht let us to find if a string is palindorme. The palindorme is that the string read from head to end and end to head are same
# First solution is complicated because it should find whether the string is even or odd and read from the middle letter very hard to thing and write
# the second in much easier just to detect whether the according to the defination
# Common solution is 
# 1 to make the letter all lower 
# 2 make the string reverse
# 3 detect whether they are the same

# In[ ]:


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L =''
        for i in s:
            if i.isalpha() or i.isdigit():
                L += i
        L = L.lower()
        a = len(L)
        if a % 2 == 0:
            first = L[0:a//2]
            second =  L[a//2:]
            if first != second[::-1]:
                return False
            return True
        
        if a % 2 != 0:
            first = L[0: int(a/2)]
            second = L[int(a/2)+1:]
            if first != second[::-1]:
                return False
            else:
                return True


# In[ ]:


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L =''
        for i in s:
            if i.isalpha() or i.isdigit():
                L += i
        L = L.lower()

        b = L[::-1]
        if L == b:
            return True
        else:
            return False
          

