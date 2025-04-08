from random_problems.binary_tree_level_order_traversal.binary_tree_level_order_traversal import (
    TreeNode,
    Solution,
)
from tests.utils import are_trees_equal


def test_traverse_double_leaf_left():
    root_tree = TreeNode(
        val=10,
        left=TreeNode(val=5, left=None, right=None),
        right=TreeNode(val=12, left=None, right=None),
    )

    reference = [10, 5, 12]

    result = Solution().levelOrder(root=root_tree)

    assert result == reference
