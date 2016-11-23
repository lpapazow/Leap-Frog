class FrogBoard:
    def __init__(self, frogs):
        self.frogs = frogs

    def __eq__(self, other):
        return self.frogs == other.frogs

    def __str__(self):
        return self.frogs

    def __repr__(self):
        return self.__str__()

    def print_board(self):
        print(self.frogs)

    def find_free_space(self):
        for idx in range(len(self.frogs)):
            if self.frogs[idx] == "_":
                return idx

    def create_new_frogboards(self):
        idx = self.find_free_space()
        new_possibilities = []
        if self.frogs[idx - 2] == ">" and idx - 2 >= 0:
            board = list(self.frogs)
            board[idx - 2], board[idx] = board[idx], board[idx - 2]
            new_possibilities.append(FrogBoard(''.join(board)))
        if self.frogs[idx - 1] == ">" and idx - 1 >= 0:
            board = list(self.frogs)
            board[idx - 1], board[idx] = board[idx], board[idx - 1]
            new_possibilities.append(FrogBoard(''.join(board)))
        try:
            if self.frogs[idx + 1] == "<":
                board = list(self.frogs)
                board[idx + 1], board[idx] = board[idx], board[idx + 1]
                new_possibilities.append(FrogBoard(''.join(board)))
        except IndexError:
            pass
        try:
            if self.frogs[idx + 2] == "<":
                board = list(self.frogs)
                board[idx + 2], board[idx] = board[idx], board[idx + 2]
                new_possibilities.append(FrogBoard(''.join(board)))
        except IndexError:
            pass
        return new_possibilities


# board = FrogBoard(">>_<<")
# print(board.find_free_space())
# for new_board in board.create_new_frogboards():
#     new_board.print_board()
#     print("Start.....................")
#     for newest in new_board.create_new_frogboards():
#         newest.print_board()
#     print("End...................")
