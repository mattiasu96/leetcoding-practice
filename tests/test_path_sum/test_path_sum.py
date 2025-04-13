from random_problems.path_sum.path_sum import TreeNode, Solution


def test_sum_is_equal_simple_tree():
    root_tree = TreeNode(
        val=10,
        left=TreeNode(val=5, left=None, right=None),
        right=TreeNode(val=12, left=None, right=None),
    )

    result = Solution().hasPathSum(root=root_tree, targetSum=15)

    assert result == True
