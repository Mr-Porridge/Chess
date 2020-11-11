# 中国象棋
class game:
    def __init__(self):
        # red 和 black 用于存储双方棋子位置(color, row, col, val)
        # 之后修改为JSON配置文件读入
        self.black = [(0, 0, 0, 1), (0, 0, 8, 1), (0, 0, 1, 2), (0, 0, 7, 2), (0, 2, 1, 3), (0, 2, 7, 3),
                      (0, 0, 4, 4), (0, 0, 3, 5), (0, 0, 5, 5), (0, 0, 2, 6), (0, 0, 6, 6), (0, 3, 0, 7),
                      (0, 3, 2, 7), (0, 3, 4, 7), (0, 3, 6, 7), (0, 3, 8, 7)]
        self.red = [(1, 9, 0, 1), (1, 9, 8, 1), (1, 9, 1, 2), (1, 9, 7, 2), (1, 7, 1, 3), (1, 7, 7, 3),
                    (1, 9, 4, 4), (1, 9, 3, 5), (1, 9, 5, 5), (1, 9, 2, 6), (1, 9, 6, 6), (1, 6, 0, 7),
                    (1, 6, 2, 7), (1, 6, 4, 7), (1, 6, 6, 7), (1, 6, 8, 7), ]
        self.chessboard = self.init_chessboard()
        self.over = False

    # 初始化棋盘
    def init_chessboard(self) -> list:
        self.chessboard = [[(-1, 0)] * 9 for _ in range(10)]
        # chessman ： (color, row, col, val)
        for chessman in self.black:
            self.set_point(chessman[0], chessman[1], chessman[2], chessman[3])
        for chessman in self.red:
            self.set_point(chessman[0], chessman[1], chessman[2], chessman[3])
        return self.chessboard

    # 设置棋子位置
    def set_point(self, color: int, row: int, col: int, val: int):
        self.chessboard[row][col] = (color, val)

    # 打印棋盘——测试
    def print_chessboard(self):
        # print("零一二三四五六七八九")
        # print("＊１２３４５６７８９")
        print("\033[31;4m＊｜１２３４５６７８９\033[0m")  # 红色
        for row in range(0, len(self.chessboard)):
            # print(row, end=" ")
            if row == 5:
                print("=====================")
                # print("\033[31;1m" + "  楚  河  汉  界  " + "\033[0m")
                # print("-------------------")
            print("\033[31;1m" + strB2Q(str(row)) + "｜\033[0m", end="")
            for point in self.chessboard[row]:
                if point[1] == 0:
                    print("＋", end="")
                    # print("－", end="")
                elif point[1] == 1:
                    print("车", end="")
                elif point[1] == 2:
                    print("马", end="")
                elif point[1] == 3:
                    print("炮", end="")
                elif point[1] == 4:
                    if point[0] == 0:
                        print("将", end="")
                    else:
                        print("帅", end="")
                elif point[1] == 5:
                    if point[0] == 0:
                        print("士", end="")
                    else:
                        print("仕", end="")
                elif point[1] == 6:
                    if point[0] == 0:
                        print("象", end="")
                    else:
                        print("相", end="")
                elif point[1] == 7:
                    if point[0] == 0:
                        print("卒", end="")
                    else:
                        print("兵", end="")
                else:
                    print("－", end="")
            print("")
        print("－－－－－－－－－－－\n")

    # 移动棋子
    def move_chessman(self, old_r: int, old_c: int, curr_r: int, curr_c: int):
        # 移动到目标位置 or 吃掉目标位置的棋子
        self.chessboard[curr_r][curr_c] = self.chessboard[old_r][old_c]
        # 原位置置空
        self.chessboard[old_r][old_c] = (-1, 0)

    # 是否可以动
    def movable(self, row: int, col: int) -> bool:
        if self.chessboard[row][col] == 0:
            return True

    # 移动规则
    # 越界（超出棋盘范围）检测

    def game_over(self) -> bool:
        return self.red[6] == [-1, 0, 0, 4] or self.black[6] == [-1, 0, 0, 4]


# 游戏玩家 红黑双方
class player:
    def __init__(self):
        self.turn = True
        self.win = False
        self.chessmen = []


def strB2Q(ustring):
    """把字符串全角转半角"""
    ss = []
    for s in ustring:
        rstring = ""
        for uchar in s:
            inside_code = ord(uchar)
            if inside_code == 32:  # 全角空格直接转换
                inside_code = 12288
            elif 33 <= inside_code <= 126:  # 全角字符（除空格）根据关系转化
                inside_code += 65248
            rstring += chr(inside_code)
        ss.append(rstring)
    return ''.join(ss)


G = game()
G.print_chessboard()
G.move_chessman(2, 1, 2, 4)
G.print_chessboard()
