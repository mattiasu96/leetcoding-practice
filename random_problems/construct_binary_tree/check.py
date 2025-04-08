preorder = [3, 9, 4, 5, 20, 15, 7]
inorder = [4, 9, 5, 3, 15, 20, 7]

mid = inorder.index(preorder[0])

sublist = preorder[1 : mid + 1]
sublist_2 = inorder[:mid]

print(mid)
print(sublist)
print(sublist_2)