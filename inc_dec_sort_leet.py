""" Increasing decreasing string
Given a string s. You should re-order the string using the following algorithm:

    Pick the smallest character from s and append it to the result.
    Pick the smallest character from s which is greater than the last appended character to the result and append it.
    Repeat step 2 until you cannot pick more characters.
    Pick the largest character from s and append it to the result.
    Pick the largest character from s which is smaller than the last appended character to the result and append it.
    Repeat step 5 until you cannot pick more characters.
    Repeat the steps from 1 to 6 until you pick all characters from s.

In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
"""
# Solution

def count_freq(s):
    # To count the frequencies of each letter and store it in a list
    freq_list = [0] * 26
    for elem in s:
        freq_list[ord(elem)-97] +=1

    print(freq_list)

    return freq_list
        
        
class Solution:
        
    def sortString(self, s: str) -> str:
        freq = count_freq(s)
        res = ''
        count = len(s)
        
        while(count >0):
            # a to z
            for i in range(26):
                # Checking whether the alphabet exists in list. then decrease count
                if(freq[i] != 0):
                    count -=1
                    res += chr(i+97)
                    freq[i] -=1
                    
            # z to a
            for i in reversed(range(26)):
                # Checking whether the alphabet exists in list. then decrease count
                if(freq[i] != 0):
                    count -=1
                    res += chr(i+97)
                    freq[i] -=1
        
        return res
