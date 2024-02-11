class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_node(self, child_node):
        self.parent = self
        self.children.append(child_node) #child_node is an instance of TreeNode

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level = level+1
            p = p.parent
        return level

    def print_tree(self):
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""

            print(prefix + self.data)
            if self.children:
                 for child in self.children:
                    child.print_tree()
"""
Electronics
    |__Laptop
        |__Macbook
        |__Dell
        |__Thinkpad
    |__Mobile
        |__iphone
        |__oneplus
    |__TV
        |__Samsung
        |__LG
"""
def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_node(TreeNode("Macbook"))
    laptop.add_node(TreeNode("Dell"))
    laptop.add_node(TreeNode("Thinkpad"))

    mobile = TreeNode("Mobile")
    mobile.add_node(TreeNode("iphone"))
    mobile.add_node(TreeNode("oneplus"))

    tv = TreeNode("TV")
    tv.add_node(TreeNode("Samsung"))
    tv.add_node(TreeNode("LG"))

    root.add_node(laptop)
    root.add_node(mobile)
    root.add_node(tv)

    root.print_tree()

if __name__ == '__main__':
     build_product_tree()

print("hi")