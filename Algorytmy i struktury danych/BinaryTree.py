class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key) + " " + str(self.val)

class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key, val):
        if self.root is None:
            self.root = Node(key, val)
        else:
            self.insert_helper(self.root, key, val)

    def insert_helper(self, node, key, val):
        if node is None:
            return Node(key, val)

        if key < node.key:
            node.left = self.insert_helper(node.left, key, val)
        elif key > node.key:
            node.right = self.insert_helper(node.right, key, val)
        else:
            node.val = val

        return node

    def search(self, key):
        if self.root is None:
            return None
        else:
            return self.search_helper(key, self.root)

    def search_helper(self, key, node):
        if node is None:
            return None

        if key == node.key:
            return node.val
        elif key < node.key:
            return self.search_helper(key, node.left)
        else:
            return self.search_helper(key, node.right)

    def delete(self, key):
        if self.root is None:
            return 0
        else:
            self.root = self.delete_helper(key, self.root)

    def delete_helper(self, key, node):
        if node is None:
            return node

        if key < node.key:
            node.left = self.delete_helper(key, node.left)
        elif key > node.key:
            node.right = self.delete_helper(key, node.right)
        else:
            if node.left is None:
                temp = node.right
                del node
                return temp
            elif node.right is None:
                temp = node.left
                del node
                return temp
            else:
                parent = node
                succ = node.right
                while succ.left is not None:
                    parent = succ
                    succ = succ.left
                if parent != node:
                    parent.left = succ.right
                else:
                    parent.right = succ.right
                node.key = succ.key
                node.val = succ.val
                del succ

        return node

    def print_helper(self, node, s):
        if node is None:
            return s
        s = self.print_helper(node.left, s)
        s += str(node) + ", "
        s = self.print_helper(node.right, s)
        return s

    def print(self):
        if self.root is None:
            return
        print(self.print_helper(self.root, ""))

    def height(self):
        return self.height_helper(self.root)

    def height_helper(self, node):
        if node is None:
            return 0
        else:
            left = self.height_helper(node.left)
            right = self.height_helper(node.right)
            return max(left, right) + 1
        
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.val)
     
            self.__print_tree(node.left, lvl+5)

tree = Tree()
tree.insert(50, "A")
tree.insert(15, "B")
tree.insert(62, "C")
tree.insert(5, "D")
tree.insert(20, "E")
tree.insert(58, "F")
tree.insert(91, "G")
tree.insert(3, "H")
tree.insert(8, "I")
tree.insert(37, "J")
tree.insert(60, "K")
tree.insert(24, "L")
tree.print_tree()
tree.print()

print (tree.search(24))
tree.insert(20, "AA")
tree.insert(6, "M")
tree.delete(62)
tree.insert(59, "N")
tree.insert(100, "P")
tree.delete(8)
tree.delete(15)
tree.insert(55, "R")
tree.delete(50)
tree.delete(5)
tree.delete(24)
tree.height()
tree.print()
tree.print_tree()


