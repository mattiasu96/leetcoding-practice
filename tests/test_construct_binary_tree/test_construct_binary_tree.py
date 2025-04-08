from random_problems.construct_binary_tree.construct_binary_tree import (
    TreeNode,
    Solution,
)
from tests.utils import are_trees_equal


def test_single_node():
    preorder = [10]
    inorder = [10]

    reference_tree = TreeNode(10, None, None)

    tree = Solution().buildTree(preorder=preorder, inorder=inorder)

    assert are_trees_equal(reference_tree, tree)


def test_balanced_tree():
    preorder = [3, 9, 4, 5, 20, 15, 7]
    inorder = [4, 9, 5, 3, 15, 20, 7]

    reference_tree = TreeNode(
        3,
        TreeNode(9, TreeNode(4, None, None), TreeNode(5, None, None)),
        TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)),
    )

    tree = Solution().buildTree(preorder=preorder, inorder=inorder)

    assert are_trees_equal(reference_tree, tree)
