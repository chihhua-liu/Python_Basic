#demo68

class Team:
    member = 7

    def working_hour(self):    # self 讓class 可以傳來傳去
        return self.day

    def all_working_hour(self):
        self.day = 7
        return self.member * self.day

    @classmethod        # only used class 本身的屬性 :  member = 7
    def get_member(cls):
        return cls.member

    @staticmethod       # 與 class 無關的function
    def calculate(x, y):
        return x ** y

        pass


t1 = Team()
print(t1.all_working_hour())
print(t1.working_hour())
print(t1.get_member())
print(t1.calculate(2, 4))