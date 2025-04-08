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
