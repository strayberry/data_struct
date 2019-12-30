# -*- coding: UTF-8

class Tree(object):
	def __init__(self, ltree=None, rtree=None, data=None):
		self.data = data
		self.ltree = ltree
		self.rtree = rtree


class BTree(object):
	def __init__(self, root=None):
		self.root = root

	def treeDepth(self, tree_root):
		if tree_root is None:
			return 0
		leftDepth = self.treeDepth(tree_root.ltree)
		rightDepth = self.treeDepth(tree_root.rtree)
		if leftDepth>=rightDepth:
			return leftDepth+1
		else:
			return rightDepth+1


if __name__=='__main__':
	tree4 = Tree(data=4)
	tree5 = Tree(data=5)
	tree2 = Tree(ltree=tree4, rtree=tree5, data=2)
	tree6 = Tree(data=6)
	tree7 = Tree(data=7)
	tree3 = Tree(ltree=tree6, rtree=tree7, data=3)
	root = Tree(ltree=tree2, rtree=tree3, data=1)
	btree = BTree(root)
	depth = btree.treeDepth(btree.root)
	print('depth:',depth)
