"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:

Input: strs = ["glower","glow","glight"]
Output: "gl"

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""
"""
Explanation

Instead of adding all alphabests as children to the trie we only add two children to the trie as we are going to find the longest common prefix and prefix ends where there are two children.
"""

class TrieNode:
    # Constructor for a node in the Trie
    def __init__(self, value = "", nxt = None, secondChild = None, is_leaf = True):
        self.value = value
        self.firstChild = nxt
        self.secondChild = secondChild
        self.is_leaf = is_leaf

def addInitialString(root, str1):
    current = root
    for char in str1:
        current.firstChild = TrieNode(char)
        current = current.firstChild
        current.is_leaf = False
    return root

def constrcuctTrie(root, n, strs):
    """ The initial string would be added to the Trie as it is. Other strings would be compared and the common prefix would be left in the tree """
    for i in range(0, n):
        elem = strs[i]
        if elem == "":
            # If any element is empty then common prefix is also empty
            root.firstChild = None
            return
        if root.firstChild == None:
            root = addInitialString(root, strs[0])
            continue
        current = root
        for char in elem:
            if current.firstChild == None :
                """ Case ["ccc", "cc"] . Trie has element c->c and current string is ccc . So the third "c" should not be added to the Trie """
                break
            elif current.firstChild.value == char:
                current = current.firstChild
            elif current.secondChild and current.secondChild.value == char:
                # Second child exists. No need to add the remaining chars of elem to Trie
                break
            else:
                # Add the second child.
                current.secondChild = TrieNode(char)
                break
        if not current.is_leaf:
            # For case ["bc", "c"]
            current.firstChild = None
            current.is_leaf = True
        
def getlongestCommonPrefix(root):
    current = root
    prefix = ""
    while current != None:
        prefix += current.value
        if current.secondChild != None:
            break
        current = current.firstChild
    return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Execution starts here.
        """
        root = TrieNode()
        n = len(strs)
        constrcuctTrie(root, n, strs)
        return getlongestCommonPrefix(root)


        
