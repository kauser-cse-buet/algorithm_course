def depth(T):
	if T is None:
		return -1
	if T.right is None and T.left is None:
		return 0
	return 1 + max(depth(T.right), depth(T.left))

class node(object):
	id = -1
	left = None
	right = None
	def _init_():

class tree(object):
	root = None
	def _init_(self):
		self.root = node()






