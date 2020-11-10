# 中国象棋
class game:
    def __init__(self):
        self.chessboard = self.init_chessboard()
        self.over = False

    # 初始化棋盘
    def init_chessboard(self):
        self.chessboard = [[0] * 9 for _ in range(10)]
        # 之后修改为JSON配置文件读入
        self.set_point(0, 0, 1)  # 黑车1
        self.set_point(0, 8, 1)  # 黑车2
        self.set_point(0, 1, 2)  # 黑马1
        self.set_point(0, 7, 2)  # 黑马2
        self.set_point(2, 1, 3)  # 黑炮1
        self.set_point(2, 7, 3)  # 黑炮2
        self.set_point(0, 4, 4)  # 黑将
        self.set_point(0, 3, 5)  # 黑士1
        self.set_point(0, 5, 5)  # 黑士2
        self.set_point(0, 2, 6)  # 黑象1
        self.set_point(0, 6, 6)  # 黑象2
        self.set_point(3, 0, 7)  # 黑卒1
        self.set_point(3, 2, 7)  # 黑卒2
        self.set_point(3, 4, 7)  # 黑卒3
        self.set_point(3, 6, 7)  # 黑卒4
        self.set_point(3, 8, 7)  # 黑卒5
        # 红方
        self.set_point(9, 0, 1)  # 黑车1
        self.set_point(9, 8, 1)  # 黑车2
        self.set_point(9, 1, 2)  # 黑马1
        self.set_point(9, 7, 2)  # 黑马2
        self.set_point(7, 1, 3)  # 黑炮1
        self.set_point(7, 7, 3)  # 黑炮2
        self.set_point(9, 4, 4)  # 黑将
        self.set_point(9, 3, 5)  # 黑士1
        self.set_point(9, 5, 5)  # 黑士2
        self.set_point(9, 2, 6)  # 黑象1
        self.set_point(9, 6, 6)  # 黑象2
        self.set_point(6, 0, 7)  # 黑卒1
        self.set_point(6, 2, 7)  # 黑卒2
        self.set_point(6, 4, 7)  # 黑卒3
        self.set_point(6, 6, 7)  # 黑卒4
        self.set_point(6, 8, 7)  # 黑卒5
        return self.chessboard

    # 设置棋子位置
    def set_point(self, row: int, col: int, val: int):
        self.chessboard[row][col] = val

    # 打印棋盘——测试
    def print_chessboard(self):
        for row in self.chessboard:
            for point in row:
                if point == 0:
                    print("－", end="")
                elif point == 1:
                    print("车", end="")
                elif point == 2:
                    print("马", end="")
                elif point == 3:
                    print("炮", end="")
                elif point == 4:
                    print("将", end="")
                elif point == 5:
                    print("士", end="")
                elif point == 6:
                    print("象", end="")
                elif point == 7:
                    print("卒", end="")
                else:
                    print("－", end="")
            print()

    # 移动棋子
    def move_chessman(self, old_r: int, old_c: int, curr_r: int, curr_c: int):
        self.chessboard[curr_c][curr_r] = self.chessboard[old_r][old_c]

    # 是否可以动
    def movable(self, row: int, col: int):
        if self.chessboard[row][col] == 0:
            return True

    # 移动规则
    # 越界（超出棋盘范围）检测


# 游戏玩家 红黑双方
class player:
    def __init__(self):
        self.turn = True
        self.win = False
        self.chessmen = []


G = game()
G.print_chessboard()
