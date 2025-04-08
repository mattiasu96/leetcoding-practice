from random_problems.right_side_view_binary_tree.right_side_view_binary_tree import (
    TreeNode,
    Solution,
)


def test_right_side_view_balanced_tree():
    root_tree = TreeNode(
        val=10,
        left=TreeNode(val=5, left=None, right=None),
        right=TreeNode(val=12, left=None, right=None),
    )

    reference = [10, 12]

    result = Solution().rightSideView(root=root_tree)

    assert result == reference
