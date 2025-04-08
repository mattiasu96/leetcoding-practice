from random_problems.k_th_smallest_value_bst.k_th_smallest_value_bst import (
    TreeNode,
    Solution,
)


def test_first_smallest_value_root():
    root_tree = TreeNode(
        val=10,
        left=TreeNode(
            val=5,
            left=TreeNode(
                val=1, left=None, right=TreeNode(val=3, left=None, right=None)
            ),
            right=None,
        ),
        right=None,
    )

    reference = 10

    result = Solution().kthSmallest(root=root_tree, k=1)

    assert result == reference


def test_smallest_in_left_only_tree():
    root_tree = TreeNode(
        val=10,
        left=TreeNode(
            val=5,
            left=TreeNode(val=1, left=None, right=None),
            right=None,
        ),
        right=None,
    )

    reference = 5

    result = Solution().kthSmallest(root=root_tree, k=2)

    assert result == reference
