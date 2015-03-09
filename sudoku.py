import copy


class Sudoku(object):

    def __init__(self):
        self.question = []
        self.answer = []
        self.temp = []
        self.level = 0

    def chuti(self):
        print("出题部分")

    def jieti(self):
        print("您输入的题目是：")
        self.answer = copy.deepcopy(self.question)
        self.show()
        print("开始解题...")
        self.temp = copy.deepcopy(self.question)
        cursor = [0, 0]
        while cursor[0] < 9:  # 行不超过9
            while cursor[1] < 9:  # 列不超过9
                # 如果游标所在格value为0
                if self.temp[cursor[0]][cursor[1]] == 0:
                    # 就将该格设为1开始尝试
                    self.temp[cursor[0]][cursor[1]] = 1
                    # 判断该格的尝试数字是否符合约束，符合则跳出循环
                    while not self.check_cell(cursor):
                        self.temp[cursor[0]][cursor[1]] += 1
                        # print(cursor)
                        if self.temp[cursor[0]][cursor[1]] > 9:
                            cursor = self.rollback(cursor)
                else:
                    pass
                cursor[1] += 1
            cursor[1] = 0
            cursor[0] += 1
        self.answer = self.temp

    def rollback(self, cursor):
        while self.temp[cursor[0]][cursor[1]] > 9:
            self.temp[cursor[0]][cursor[1]] = 0
            while True:
                cursor[1] -= 1
                if cursor[1] == -1:
                    cursor[0] -= 1
                    cursor[1] = 8
                if int(self.question[cursor[0]][cursor[1]])== 0 or cursor == [0, 0]:
                    break
            self.temp[cursor[0]][cursor[1]] += 1
        return cursor

    def check_cell(self, cursor):
        row = cursor[0]  # 行名ABC
        line = cursor[1]  # 列名123
        value = self.temp[row][line]
        # 先检查行
        for i in range(0, 9):
            if i == line:
                continue
            if self.temp[row][i] == value:
                return False
        # 再检查列
        for i in range(0, 9):
            if i == row:
                continue
            if self.temp[i][line] == value:
                return False
        # 再检查宫
        for i in range(0, 3):  # 宫里的行
            for j in range(0, 3):  # 宫里的列
                row_n = cursor[0] - cursor[0] % 3 + i
                line_n = cursor[1] - cursor[1] % 3 + j
                if row_n == cursor[0] and line_n == cursor[1]:
                    continue
                if self.temp[row_n][line_n] == value:
                    return False
        # 检查都过了
        return True

    def check_cell_available(self, cursor):
        pass

    def show(self):
        for i in range(0, 9):
            string = ""
            for j in range(0, 9):
                string += ' ' + str(
                    self.answer[i][j])
                if (j + 1) % 3 == 0:
                    string += " |"
            print(string)
            if (i + 1) % 3 == 0:
                print("------------------------")
