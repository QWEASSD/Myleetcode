
# coding: utf-8

# ### 566. Reshape the Matrix
# In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.
# 
# You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
# 
# The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
# 
# If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
# '''
# Input: 
# nums = 
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# Output: 
# [[1,2,3,4]]
# Explanation:
# The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
# '''
# 

# use two for loop, the outside one control the row and the inside one control the column
# 
# step 1:
# extract the element from the origan list and make it reverse
# step 2:
# make the two loop 
# step 3:
# insert the value to the column by using the pop()
# 

# In[ ]:


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        l = len(nums)
        h = len(nums[0])
        if l*h != r*c:
            return nums
        else:
            L =[]
            for i in nums:
                for j in i:
                    L.append(j)
            L.reverse()
            
            a = []
            for j in range(r):
                b = []
                for h in range(c):
                    b.append(L.pop())
                a.append(b)
            return a

