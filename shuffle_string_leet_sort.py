# Question
1528. Shuffle string
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

# Soultion

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # New list. Using list to store the result since string is immutable.
        list1 = indices.copy()
        for i in range(len(indices)):
            # Adding elements to new array in the correct order
            list1[indices[i]] = s[i]
        
        # FRom list to string. 
        listToStr = ''.join([str(elem) for elem in list1]) 
        
        return listToStr
