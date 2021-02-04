# range sum of BST
# Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def in_order_traversal(node):
    """
    Do in order traversal on the tree and return the sorted list
    """
    res_list = []
    if(node!=None and node.val!="null"):
        res_list.extend(in_order_traversal(node.left))
        res_list.append(node.val)
        res_list.extend(in_order_traversal(node.right))
    return res_list

def binary_search(arr, low, high, x):
    """
    Find the index of the element in the sorted_list using binary search 
    and return the index
    """
    if high >= low:

    	mid = (high + low)//2
    	if arr[mid] == x:
    		return mid
    
    	elif arr[mid] > x:
    		return binary_search(arr, low, mid - 1, x)
    	else:
    		return binary_search(arr, mid + 1, high, x)
    
    
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        """
        Get the elements soretd using in oder traversla on binary search tree. Get the starting index         using binary search. Adding until high value comes. Return the sum
        """
        sum = 0
        sorted_list = in_order_traversal(root)
        print(sorted_list)
        i = binary_search(sorted_list, 0, len(sorted_list)-1, low)
        print(i)
        while(i<len(sorted_list)):
            sum+= sorted_list[i]
            if(sorted_list[i]== high):
                break
            i+=1
        
        return sum
        
