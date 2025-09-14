"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""
"""
Solution 1 using greedy. BFS is performed on the array.
Time complexity : O(n)
Space complexity : O(1)
https://www.youtube.com/watch?v=dJ7sWiOoK7g
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Uses greedy approach. BFS on each level. While loop is to change levels and for loop is to loop on elements in a level.
        """
        n = len(nums)
        l = r = 0
        no_jump = 0

        while r < n-1 :
            farthest = 0
            for i in range (l, r+1):
                farthest = max (nums[i] + i, farthest)
            l = r + 1
            r = farthest
            no_jump +=1

        return no_jump
"""
Solution 2 using dynamic programming. Array to store min jumps at each index.
Time complexity : O(n * n)
Space complexity : O(n)
https://www.youtube.com/watch?v=PrSi5u0KMyE
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        # dp[i] means the minimum number of jumps to reach index i
        # for each dp[i]，we need to find the earliest j that can reach i from j
        # dp[i] = dp[j] + 1
        
        dp = [0] * n
        j = 0
        for i in range(1, n):
            while j + nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1
        
        return dp[-1]
