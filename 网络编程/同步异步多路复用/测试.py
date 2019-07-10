
# 河南  张前鹏 2019/6/20 星期四 11:00:59


class Tank:
    def __init__(self, x, y, dire):
        self.x = x
        self.y = y
        self.dire = dire
        self.P = True

    def signal(self, src: str):
        for i in src:
            # print(self.x, self.y)
            if i == "M":
                self.go()
            if i == "T":  # 时间同步不动?
                pass
            if i == "P":
                self.P = False if self.P else True
            else:
                self.turn_round(i)

    def turn_round(self, src):
        if src == "L":  # 左
            if self.P:  # 正
                if self.dire == "W":  # 西
                    self.dire = "S"  # 南
                elif self.dire == "E":  # 东
                    self.dire = "N"  # 北
                elif self.dire == "N":
                    self.dire = "W"
                elif self.dire == "S":
                    self.dire = "E"
            else:
                if self.dire == "W":
                    self.dire = "N"
                elif self.dire == "E":
                    self.dire = "S"
                elif self.dire == "N":
                    self.dire = "E"
                elif self.dire == "S":
                    self.dire = "W"
        if src == "R":  # 右
            if self.P:
                if self.dire == "W":
                    self.dire = "N"
                elif self.dire == "E":
                    self.dire = "S"
                elif self.dire == "N":
                    self.dire = "E"
                elif self.dire == "S":
                    self.dire = "W"
            else:
                if self.dire == "W":
                    self.dire = "S"
                elif self.dire == "E":
                    self.dire = "N"
                elif self.dire == "N":
                    self.dire = "W"
                elif self.dire == "S":
                    self.dire = "E"

    def go(self):
        if self.dire == "W":
            self.x = self.x - 1
            # print(self.x,self.y)
        elif self.dire == "E":
            self.x = self.x + 1
            # print(self.x, self.y)
        elif self.dire == "N":
            self.y = self.y + 1
            # print(self.x, self.y)
        elif self.dire == "S":
            self.y = self.y - 1
            # print(self.x, self.y)

    def show(self):
        print("x:{},y:{}".format(self.x, self.y))


t = Tank(11, 39, "W")
t.signal("MTMPRPMTMLMRPRMTPLMMTLMRRMP")
t.show()
