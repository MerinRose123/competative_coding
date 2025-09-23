from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Traversals:
    # -------------------------------
    # Inorder Traversal (Left → Root → Right)
    # -------------------------------
    def inorder_recursive(self, root: TreeNode) -> list[int]:
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result

    def inorder_iterative(self, root: TreeNode) -> list[int]:
        result, stack, current = [], [], root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result

    def inorder_morris(self, root: TreeNode) -> list[int]:
        result, current = [], root
        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right
        return result

    # -------------------------------
    # Preorder Traversal (Root → Left → Right)
    # -------------------------------
    def preorder_recursive(self, root: TreeNode) -> list[int]:
        result = []
        def preorder(node):
            if not node:
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return result

    def preorder_iterative(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def preorder_morris(self, root: TreeNode) -> list[int]:
        result, current = [], root
        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                if not predecessor.right:
                    result.append(current.val)  # visit before going left
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    current = current.right
        return result

    # -------------------------------
    # Postorder Traversal (Left → Right → Root)
    # -------------------------------
    def postorder_recursive(self, root: TreeNode) -> list[int]:
        result = []
        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
        postorder(root)
        return result

    def postorder_iterative(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        stack1, stack2, result = [root], [], []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            result.append(stack2.pop().val)
        return result

    def postorder_morris(self, root: TreeNode) -> list[int]:
        result = []

        def reversePath(start, end):
            if start == end:
                return
            x, y, z = start, start.right, None
            while True:
                z = y.right
                y.right = x
                x, y = y, z
                if x == end:
                    break

        def printReverse(start, end):
            reversePath(start, end)
            node = end
            while True:
                result.append(node.val)
                if node == start:
                    break
                node = node.right
            reversePath(end, start)

        dummy = TreeNode(0)
        dummy.left = root
        current = dummy

        while current:
            if current.left:
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    printReverse(current.left, predecessor)
                    predecessor.right = None
                    current = current.right
            else:
                current = current.right

        return result

    # -------------------------------
    # Level Order Traversal (BFS)
    # -------------------------------
    def level_order(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        result, queue = [], deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    # Build a sample tree:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))

    t = Traversals()

    print("Inorder (recursive):", t.inorder_recursive(root))
    print("Inorder (iterative):", t.inorder_iterative(root))
    print("Inorder (Morris):", t.inorder_morris(root))

    print("Preorder (recursive):", t.preorder_recursive(root))
    print("Preorder (iterative):", t.preorder_iterative(root))
    print("Preorder (Morris):", t.preorder_morris(root))

    print("Postorder (recursive):", t.postorder_recursive(root))
    print("Postorder (iterative):", t.postorder_iterative(root))
    print("Postorder (Morris):", t.postorder_morris(root))

    print("Level Order (BFS):", t.level_order(root))
