'''
This file implements the Binary Search Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree file.
'''

from Trees.BinaryTree import BinaryTree, Node

class BST(BinaryTree):
    '''
    FIXME:
    BST is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above 
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''
        super().__init__()
        if xs is not None:
            self.insert_list(xs)

        #this is the same as BinaryTree.__init__(self)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command BST([1,2,3])
        it's __repr__ will return "BST([1,2,3])"

        For the BST, type(self).__name__ will be the string "BST",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of BST will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__+'('+str(self.to_list('inorder'))+')'


    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        FIXME:
        Implement this method.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        is_left_satisfied = True
        is_right_satisfied = True
        if node.left:
            if node.value > node.left.value:
                is_left_satisfied  =  BST._is_bst_satisfied(node.left)
            else:
                is_left_satisfied = False
        if node.right:
            if node.value < node.right.value:
                is_right_satisfied  = BST._is_bst_satisfied(node.right)
            else:
                is_right_satisfied = False
        return is_left_satisfied and is_right_satisfied


    def insert(self, value):
        '''
        Inserts value into the BST.
        '''
        if self.root is None:
            self.root = Node(value)
        else:
            BST._insert(value, self.root)


    @staticmethod
    def _insert(value, node):
        '''
        FIXME:
        Implement this function.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
      #  if value < node, self.root.value:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                BST._insert(value, node.left)

        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                BST._insert(value, node.right)

        else:
            print("value is already in tree")


    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.
        '''
        #how do I test using pytest? 
        #Can I use a forloop here? also confused on remove list, probably need to do rmeove first
        for a in xs:
            self.insert(a)  #I use  insert not _insert right? do i need to return something? 

    def __contains__(self, value):
        return self.find(value)


    def find(self, value):
        '''
        Returns whether value is contained in the BST.
        '''
        if self.root:
            if BST._find(value, self.root):
                return True
        else:
            return False

    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        if value > node.value and node.right:
            return BST._find(value, node.right)
        elif value < node.value and node.left:
            return BST._find(value, node.left)
        if value == node.value:
            return True
        else:
            return False

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
        This function is not implemented in the lecture notes,
        but if you understand the structure of a BST it should be easy to implement.

        HINT:
        Create a recursive staticmethod helper function,
        similar to how the insert and find functions have recursive helpers.
        '''
        if self.root is None:
            raise ValueError("nothing in tree")
        else:
            return BST._find_smallest(self.root)

    
    
    @staticmethod
    def _find_smallest(node):
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)



    def find_largest(self):
        '''
        Returns the largest value in the tree.

        FIXME:
        Implement this function.
        This function is not implemented in the lecture notes,
        but if you understand the structure of a BST it should be easy to implement.
        '''
        if self.root is None:
            raise ValueError("nothing in tree")
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def  _find_largest(node):
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)


    def remove(self,value):
        '''
        Removes value from the BST. 
        If value is not in the BST, it does nothing.

        FIXME:
        implement this function.
        There is no code given in any of the lecture videos on how to implement this function,
        but the video by HMC prof Colleen Lewis explains the algorithm.

        HINT:
        You must have find_smallest/find_largest working correctly 
        before you can implement this function.

        HINT:
        Use a recursive helper function.
        ''' 
        self.root = BST._remove(self.root,value)

    @staticmethod
    def _remove(node, value):
       # print("node=", node)
        if node is None:
            return
        if node.value > value:
            node.left = BST._remove(node.left, value)
        elif node.value < value:
            node.right =  BST._remove(node.right, value)
        else:
            if not node.left and not node.right:
                return None
            if node.left and not node.right:
                return node.left
            if node.right and not node.left:
                return node.right
        #    print("node.right =", node.right)
            left_most = BST._find_smallest(node.right) 
            #node.right.find_smallest() #is this the right way to call find_smallest?
            node.value = left_most
            node.right = BST._remove(node.right, node.value)
        return node
    
    
    def remove_list(self, xs): #does this look right? 
        '''
        Given a list xs, remove each element of xs from self.

        FIXME:
        Implement this function.
        '''
        for a in xs:
            self.remove(a)

bst = BST()
bst.root = Node(0)
bst.root.left = Node(-2)
bst.root.left.left = Node(-3)
bst.root.left.right = Node(-1)
bst.root.right = Node(2)
bst.root.right.left = Node(1)
bst.root.right.right = Node(-3)
