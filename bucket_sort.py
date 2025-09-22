"""
451. Sort Characters By Frequency

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Constraints:
1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
"""
"""
Approach: Bucket Sort
1. Create bucket for each frequency from 1 to max(freq)
2. Iterate thorugh the bucket and form the result
"""
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        result = []
        counter = Counter(s)
        max_freq = max(counter.values())

        buckets = [[] for _ in range(max_freq+1)]

        for elem, freq in counter.items():
            buckets[freq].append(elem)
        
        for freq in range(max_freq, 0, -1):
            for elem in buckets[freq]:
                result.append(elem * freq)
        
        return "".join(result)
