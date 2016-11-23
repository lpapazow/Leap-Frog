from tree import Tree
from frog_board import FrogBoard


class FrogBoardTree(Tree):
    def __init__(self, frogs):
        start_str = self.create(frogs)
        Tree.__init__(self, FrogBoard(start_str))
        self.add_children(self.root)

    def add_children(self, node):
        children = node.value.create_new_frogboards()
        for child in children:
            node.add_child(child)
            self.add_children(node.get_last_child())

    def create(self, frogs):
        res = ""
        for i in range(frogs):
            res += '>'
        res += '_'
        for i in range(frogs):
            res += '<'
        return res
