from random_problems.binary_tree_inorder_traversal.binary_tree_in_order_traversal import (
    TreeNode,
    Solution,
)


def are_trees_equal(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    if tree1.val != tree2.val:
        return False
    return are_trees_equal(tree1.left, tree2.left) and are_trees_equal(
        tree1.right, tree2.right
    )


def test_traverse_single_root():
    root_tree = TreeNode(val=10, left=None, right=None)

    reference = [10]

    result = Solution().inorderTraversal(root=root_tree)

    assert result == reference


def test_traverse_single_leaf_left():
    root_tree = TreeNode(
        val=10, left=TreeNode(val=5, left=None, right=None), right=None
    )

    reference = [5, 10]

    result = Solution().inorderTraversal(root=root_tree)

    assert result == reference


def test_traverse_double_leaf_left():
    root_tree = TreeNode(
        val=10,
        left=TreeNode(val=5, left=None, right=None),
        right=TreeNode(val=12, left=None, right=None),
    )

    reference = [5, 10, 12]

    result = Solution().inorderTraversal(root=root_tree)

    assert result == reference


def test_traverse_multi_level_tree():
    root_tree = TreeNode(
        val=10,
        left=TreeNode(
            val=5,
            left=TreeNode(val=1, left=None, right=None),
            right=TreeNode(val=3, left=None, right=None),
        ),
        right=TreeNode(val=12, left=None, right=None),
    )

    reference = [1, 5, 3, 10, 12]

    result = Solution().inorderTraversal(root=root_tree)

    assert result == reference
