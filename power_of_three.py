# Power of Three

# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

 

# Example 1:

# Input: n = 27
# Output: true

# Example 2:

# Input: n = 0
# Output: false

# Example 3:

# Input: n = 9
# Output: true

# Example 4:

# Input: n = 45
# Output: false

# Constraints:

#     -231 <= n <= 231 - 1


# Code
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Divide by 3 untill the number becomes 3 raise to 0
        while(n >= 3):
            if n % 3 == 0:
                n = int(n/3)
            else:
                return False
            
        # If the number is one then it is power of 3 else not
        if n == 1:
            return True
        else:
            return False
