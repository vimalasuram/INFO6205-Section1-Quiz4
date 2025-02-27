import unittest
from bst import TreeNode, search_bst

class TestBSTSearch(unittest.TestCase):
    
    def test_empty_tree(self):
        """Test when the tree is empty"""
        self.assertFalse(search_bst(None, 5))
    
    def test_single_node_tree_found(self):
        """Test when tree has only one node and value is found"""
        root = TreeNode(5)
        self.assertTrue(search_bst(root, 5))
    
    def test_single_node_tree_not_found(self):
        """Test when tree has only one node and value is not found"""
        root = TreeNode(5)
        self.assertFalse(search_bst(root, 10))
    
    def test_multiple_nodes_found(self):
        """Test when tree has multiple nodes and value is found"""
        root = TreeNode(8)
        root.left = TreeNode(3)
        root.right = TreeNode(10)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.right.right = TreeNode(14)
        
        self.assertTrue(search_bst(root, 10))
        self.assertTrue(search_bst(root, 1))
        self.assertTrue(search_bst(root, 6))
    
    def test_multiple_nodes_not_found(self):
        """Test when tree has multiple nodes and value is not found"""
        root = TreeNode(8)
        root.left = TreeNode(3)
        root.right = TreeNode(10)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.right.right = TreeNode(14)
        
        self.assertFalse(search_bst(root, 7))
        self.assertFalse(search_bst(root, 13))
        self.assertFalse(search_bst(root, 4))
    
    def test_left_heavy_tree(self):
        """Test a left-heavy tree structure"""
        root = TreeNode(10)
        root.left = TreeNode(8)
        root.left.left = TreeNode(6)
        root.left.left.left = TreeNode(4)
        root.left.left.left.left = TreeNode(2)
        
        self.assertTrue(search_bst(root, 2))
        self.assertTrue(search_bst(root, 6))
        self.assertFalse(search_bst(root, 7))
        self.assertFalse(search_bst(root, 1))
    
    def test_right_heavy_tree(self):
        """Test a right-heavy tree structure"""
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.right = TreeNode(5)
        root.right.right.right = TreeNode(7)
        root.right.right.right.right = TreeNode(9)
        
        self.assertTrue(search_bst(root, 9))
        self.assertTrue(search_bst(root, 3))
        self.assertFalse(search_bst(root, 6))
        self.assertFalse(search_bst(root, 10))
    
    def test_balanced_tree(self):
        """Test a balanced tree structure"""
        # Creating a balanced tree:
        #        8
        #      /   \
        #     4     12
        #    / \    / \
        #   2   6  10  14
        root = TreeNode(8)
        root.left = TreeNode(4)
        root.right = TreeNode(12)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(6)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(14)
        
        # Test all values in the tree
        self.assertTrue(search_bst(root, 8))
        self.assertTrue(search_bst(root, 4))
        self.assertTrue(search_bst(root, 12))
        self.assertTrue(search_bst(root, 2))
        self.assertTrue(search_bst(root, 6))
        self.assertTrue(search_bst(root, 10))
        self.assertTrue(search_bst(root, 14))
        
        # Test values not in the tree
        self.assertFalse(search_bst(root, 1))
        self.assertFalse(search_bst(root, 3))
        self.assertFalse(search_bst(root, 5))
        self.assertFalse(search_bst(root, 7))
        self.assertFalse(search_bst(root, 9))
        self.assertFalse(search_bst(root, 11))
        self.assertFalse(search_bst(root, 13))
        self.assertFalse(search_bst(root, 15))
    
    
    def test_negative_values(self):
        """Test with negative values"""
        root = TreeNode(0)
        root.left = TreeNode(-5)
        root.right = TreeNode(5)
        root.left.left = TreeNode(-10)
        root.left.right = TreeNode(-2)
        
        self.assertTrue(search_bst(root, -5))
        self.assertTrue(search_bst(root, -2))
        self.assertFalse(search_bst(root, -3))
    
    def test_large_values(self):
        """Test with large integer values"""
        root = TreeNode(1000)
        root.left = TreeNode(100)
        root.right = TreeNode(10000)
        
        self.assertTrue(search_bst(root, 10000))
        self.assertFalse(search_bst(root, 5000))

if __name__ == '__main__':
    unittest.main()