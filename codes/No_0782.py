#
# @lc app=leetcode.cn id=782 lang=python3
#
# [782] 变为棋盘
#


# @lc code=start
class Solution:
    def movesToChessboard(self, board) -> int:
        # basic parameters define
        dimension = len(board)
        nfloor = dimension // 2
        nceil = nfloor + 1 if dimension % 2 else nfloor

        # 1. check row and col sumup value
        for row in board:
            if sum(row) not in [nfloor, nceil]:
                return -1

        for ncol in range(dimension):
            count = sum([row[ncol] for row in board])
            if count not in [nfloor, nceil]:
                return -1

        # 2. check reverse-able
        # row - mode
        for row in board:
            count = sum([i == j for i, j in zip(board[0], row)])
            if count not in [0, dimension]:
                return -1

        # col - mode
        for ncol in range(dimension):
            count = sum([
                board[ncol][nrow] == board[0][nrow]
                for nrow in range(dimension)
            ])
            if count not in [0, dimension]:
                return -1

        # 3. find mismatch part
        nrow = self.number_of_swap(board[0])
        ncol = self.number_of_swap([row[0] for row in board])
        return nrow + ncol

    def number_of_swap(self, vector):
        zeros, ones = 0, 0
        for idx, val in enumerate(vector):
            if (val + idx) % 2:
                zeros = zeros + 1
            else:
                ones = ones + 1

        zeros = len(vector) if zeros % 2 else zeros
        ones = len(vector) if ones % 2 else ones
        return min(zeros, ones) // 2


if __name__ == '__main__':
    print(Solution().movesToChessboard([[1, 1, 0], [0, 0, 1], [0, 0, 1]]))
    print(Solution().movesToChessboard([[0, 1, 1, 0], [0, 1, 1, 0],
                                        [1, 0, 0, 1], [1, 0, 0, 1]]))
    print(Solution().movesToChessboard([[0, 0, 1, 1], [1, 1, 0, 0],
                                        [0, 1, 0, 1], [1, 0, 1, 0]]))

# @lc code=end
