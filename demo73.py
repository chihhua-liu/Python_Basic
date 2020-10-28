#demo72

class Emp:
    gradeLevel = 6

    def startWork(self):
        pass

    def endWork(self):
        pass


class RD(Emp):
    def __init__(self):
        self.currentGrade = self.gradeLevel

    def startWork(self):
        print(f"[{self.currentGrade}] start to work")
    def endWork(self):
        print(f"[{self.currentGrade}] finish work")

rd1 = RD()
rd1.startWork()
rd1.currentGrade = 7
rd1.startWork()
print(rd1.currentGrade, rd1.gradeLevel)
rd1.gradeLevel = 5
rd1.startWork()
print(rd1.currentGrade, rd1.gradeLevel, Emp.gradeLevel)