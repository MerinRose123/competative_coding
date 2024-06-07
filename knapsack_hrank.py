# Given an array of integers and a target sum, determine the sum nearest to but not exceeding the target that can be created. To create the sum, use any element of your array zero or more times.

# For example, if
# and your target sum is , you might select or

# . In this case, you can arrive at exactly the target.

# Function Description

# Complete the unboundedKnapsack function in the editor below. It must return an integer that represents the sum nearest to without exceeding the target value.

# unboundedKnapsack has the following parameter(s):

#     k: an integer
#     arr: an array of integers

# Input Format

# The first line contains an integer

# , the number of test cases.

# Each of the next
# pairs of lines are as follows:
# - The first line contains two integers and , the length of and the target sum.
# - The second line contains space separated integers

# .

# Constraints


# Output Format

# Print the maximum sum for each test case which is as near as possible, but not exceeding, to the target sum on a separate line.

# Sample Input

# 2
# 3 12
# 1 6 9
# 5 9
# 3 4 4 4 8

# Sample Output

# 12
# 9

# Explanation

# In the first test case, one can pick {6, 6}. In the second, we can pick {3,3,3}.


# Answer
#!/bin/python3

import math
import os
import random
import re
import sys

def unboundedKnapsack(k, arr):
        """
    Using the tabulation method in dynamic programming. An array sum_array of the size of taregtsum + 1 is created and sum 
    is calculated usign iteration from zero.
    """
    sum_array = [None] * (k + 1)
    n = len(arr)
    sum_array[0] = True
    
    for i in range(k):
        if sum_array[i]:
            for num in arr:
                if(i+num <= k):
                    sum_array[i + num] = True
    
    # Returning the most close but lower or equal so
    j = k
    while(j >= 0):
        if sum_array[j]:
            return j
        j -= 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    i = 0
    while i < t:
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)
        
        i +=1

        fptr.write(str(result) + '\n')

    fptr.close()

