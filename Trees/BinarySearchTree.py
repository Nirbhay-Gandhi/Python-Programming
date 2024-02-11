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
    print("in-order: ",res_inorder)    
    print("pre-order: ",res_preorder)    
    print("post-order: ",res_postorder)    