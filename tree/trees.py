class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def add_node_iterative(self, key, val):
        if self.root is None:
            self.root = TreeNode(key, val)

        curr_node = self.root
        while curr_node:
            if key < curr_node.key:
                if curr_node.has_left_child():
                    curr_node = curr_node.left_child
                else:
                    curr_node.left_child = TreeNode(key, val, parent=curr_node)
            elif key > curr_node.key:
                if curr_node.has_right_child():
                    curr_node = curr_node.right_child
                else:
                    curr_node.right_child = TreeNode(key, val, parent=curr_node)
            else:
                curr_node.val = val

    def add_node_recursive(self, key, val):
        if self.root is None:
            self.root = TreeNode(key, val)
        else:
            self._add_node_recursive(key, val, self.root)

    def _add_node_recursive(self, key, val, curr_node):
        lc = curr_node.has_left_child()
        rc = curr_node.has_right_child()

        if key < curr_node.key:
            if lc:
                self._add_node_recursive(key, val, lc)
            else:
                curr_node.left_child = TreeNode(key, val, parent=curr_node)
            self.size += 1
        elif key > curr_node.key:
            if rc:
                self._add_node_recursive(key, val, rc)
            else:
                curr_node.right_child = TreeNode(key, val, parent=curr_node)
            self.size += 1
        else:
            curr_node.val = val

    def get_iterative(self, key):
        curr_node = self.root
        while curr_node:
            if key == curr_node.key:
                return curr_node
            elif key < curr_node.key:
                curr_node = curr_node.left_child
            else:
                curr_node = curr_node.right_child

        return None

    def get_recursive(self, key):
        if self.root is None:
            return None
        return self._get_recursive(key, self.root)

    def _get_recursive(self, key, curr_node):
        if not curr_node:
            return None
        elif key < curr_node.val:
            return self._get_recursive(key, curr_node.left_child)
        elif key > curr_node.val:
            return self._get_recursive(key, curr_node.right_child)
        else:
            return curr_node

    def length(self):
        return self.size

    def __setitem__(self, key, value):
        self.add_node_recursive(key, value)

    def __getitem__(self, key):
        return self.get_recursive(key)

    def __contains__(self, key):
        return True if self._get_recursive(key, self.root) else False

    def __len__(self):
        return self.size


class TreeNode:

    def __init__(self, key, val, parent=None, lc=None, rc=None):
        self.key = key
        self.val = val
        self.parent = parent
        self.left_child = lc
        self.right_child = rc

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_root(self):
        return self.parent is None
