from random_problems.delete_node_in_bts.delete_node_in_bts import TreeNode, Solution
from tests.utils import are_trees_equal


def test_delete_root_node_tree():
    root_tree = TreeNode(val=10, left=None, right=None)

    new_tree = Solution().deleteNode(root=root_tree, key=10)

    reference = None

    assert are_trees_equal(reference, new_tree)


def test_delete_leaf():
    root_tree = TreeNode(
        val=10,
        left=TreeNode(val=5, left=None, right=None),
        right=TreeNode(val=12, left=None, right=None),
    )

    new_tree = Solution().deleteNode(root=root_tree, key=5)

    reference = TreeNode(
        val=10,
        left=None,
        right=TreeNode(val=12, left=None, right=None),
    )

    assert are_trees_equal(reference, new_tree)


def test_delete_node_with_one_child():
    root_tree = TreeNode(
        val=10,
        left=TreeNode(val=5, left=TreeNode(val=3, left=None, right=None), right=None),
        right=TreeNode(val=12, left=None, right=None),
    )

    new_tree = Solution().deleteNode(root=root_tree, key=5)

    reference = TreeNode(
        val=10,
        left=TreeNode(val=3, left=None, right=None),
        right=TreeNode(val=12, left=None, right=None),
    )

    assert are_trees_equal(reference, new_tree)


def test_delete_node_with_two_children():
    root_tree = TreeNode(
        val=10,
        left=TreeNode(
            val=5,
            left=TreeNode(val=3, left=None, right=None),
            right=TreeNode(val=7, left=None, right=None),
        ),
        right=TreeNode(val=12, left=None, right=None),
    )

    new_tree = Solution().deleteNode(root=root_tree, key=5)

    reference = TreeNode(
        val=10,
        left=TreeNode(val=7, left=TreeNode(val=3, left=None, right=None), right=None),
        right=TreeNode(val=12, left=None, right=None),
    )

    assert are_trees_equal(reference, new_tree)
