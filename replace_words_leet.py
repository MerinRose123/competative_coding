"""
Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
 

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
"""
"""
Explanation

Use a trie to store the dictionary. Then for each word in the sentense traverse the trie.

Time complexity:
O(nk+mk)O(nk + mk)O(nk+mk)
n - Length of the sentence excluding space
m - Length of dictionary
k - Max length of word in root dictionary

"""
class TrieNode:
    def __init__(self, wordEnd = False):
        self.wordEnd = wordEnd
        self.children = [None]*26


def constructTrie(root, dictionary):
    for word in dictionary:
        current = root
        for char in word:
            index = ord(char) - ord('a')
            if current.children[index] == None:
                current.children[index] = TrieNode()
                current = current.children[index]
            else:
                current = current.children[index]
        current.wordEnd = True


def getRootWord(root, word):
    rootWord = ""
    current = root
    for i, char in enumerate(word):
        index = ord(char) - ord('a')
        if current.children[index] != None:
            rootWord += chr(97 + index)
            current = current.children[index]
        elif not current.wordEnd:
            return word
        if current.wordEnd:
            break
    return rootWord


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentenceList = sentence.split(" ")
        root = TrieNode()
        constructTrie(root, dictionary)
        for i, word in enumerate(sentenceList):
            rootWord = getRootWord(root, word)
            if not rootWord == "":
                sentenceList[i] = rootWord
        return " ".join(sentenceList)
        
