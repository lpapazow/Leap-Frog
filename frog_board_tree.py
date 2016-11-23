from tree import Tree
from FrogBoard import FrogBoard


class FrogBoardTree(Tree):
    def __init__(self, frogs):
        strat_str = self.create(frogs)
        Tree.__init__(start_str)

    def create(self, frogs):
        res = ""
        for i in range(frogs):
            res += '>'
        res += '_'
        for i in range(frogs):
            res += '<'
        return res
