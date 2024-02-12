# from collections import queue

class TreeNode:
    def __init__(self, data):
        self.left_node = None #instance of TreeNode
        self.right_node = None #instance of TreeNode
        self.data = data

    def insert(self, data):
        if data == self.data: #the element already exists, do nothing
            return
        else:
            #Left
            if data < self.data:
                if self.left_node is None: #you are in leaf node
                    self.left_node = TreeNode(data) 
                else: 
                    self.left_node.insert(data) #self.left_node is another subtree
            #Right
            else:
                if self.right_node is None:
                    self.right_node = TreeNode(data)
                else:
                    self.right_node.insert(data)

    #Printing - Inorder : LeftSmallTree -> Root -> RightSmallTree
    def print_inorder(self, root):
        res = []
        if root:
            res = self.print_inorder(root.left_node)
            res.append(root.data)
            res = res + self.print_inorder(root.right_node)
        return res
    
    #Printing - Preorder : root -> LeftSmallTree -> RightSmallTree
    def print_preorder(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.print_inorder(root.left_node)
            res = res + self.print_inorder(root.right_node)
        return res
    
    #Printing - Postorder : LeftSmallTree -> RightSmallTree -> Root
    def print_postorder(self, root):
        res = []
        if root:
            res = res + self.print_inorder(root.left_node)
            res = res + self.print_inorder(root.right_node)
            res.append(root.data)
        return res
    

    def print_levelorder(self, root):
        if root is None:
            return []
        
        queue = []
        result = []
        queue.append(root)
        
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.data)
            result.append(node.data)

            if node.left_node:
                self.print_levelorder(node.left_node)
            if node.right_node:
                self.print_levelorder(node.right_node)
        return result

    def level_order_traversal(self, root):
        if root is None:
            return []

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            result.append(node.data)

            if node.left_node:
                queue.append(node.left_node)
            if node.right_node:
                queue.append(node.right_node)

        return result
    
def buildTree(elements):
    root = TreeNode(elements[0])
    for i in range(1,len(elements)):
        root.insert(elements[i])
    return root 
    

if __name__ == '__main__':
    elements = [1,7,3,5,2,-4,9,6]
    root = buildTree(elements)

    res_inorder = root.print_inorder(root)
    res_preorder = root.print_preorder(root)
    res_postorder = root.print_postorder(root)
    res_levelorder = root.level_order_traversal(root)
    print("in-order: ",res_inorder)    
    print("pre-order: ",res_preorder)    
    print("post-order: ",res_postorder)    
    print("level-order: ",res_levelorder)    