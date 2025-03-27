from random_problems.insert_binary_search_tree.insert_binary_search_tree import (
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


insertion_node = TreeNode(val=10, left=None, right=None)


def test_insert_in_empty_tree():
    reference_tree = TreeNode(val=10, left=None, right=None)

    new_tree = Solution().insertIntoBST(root=None, val=10)

    assert are_trees_equal(reference_tree, new_tree)


def test_insert_in_tree_with_root():
    base_tree = TreeNode(val=10, left=None, right=None)

    reference_tree = TreeNode(
        val=10,
        left=TreeNode(val=5, left=None, right=None),
        right=TreeNode(val=12, left=None, right=None),
    )

    new_tree = Solution().insertIntoBST(root=base_tree, val=5)
    new_tree = Solution().insertIntoBST(root=new_tree, val=12)

    assert are_trees_equal(reference_tree, new_tree)


def test_insert_in_tree_with_multiple_layers():
    base_tree = TreeNode(val=10, left=None, right=None)

    reference_tree = TreeNode(
        val=10,
        left=TreeNode(val=5, left=TreeNode(val=2, left=None, right=None), right=None),
        right=TreeNode(val=12, left=None, right=None),
    )

    new_tree = Solution().insertIntoBST(root=base_tree, val=5)
    new_tree = Solution().insertIntoBST(root=new_tree, val=12)
    new_tree = Solution().insertIntoBST(root=new_tree, val=2)

    assert are_trees_equal(reference_tree, new_tree)
