from random_problems.delete_node_in_bts.delete_node_in_bts import TreeNode, Solution


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
