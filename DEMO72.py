#demo71

class Emp(object):
    gradeLevel = 6

    def startWork(self):
        pass

    def endWork(self):
        pass

    pass


class RD(Emp):
    pass


class PM(Emp):
    pass


print(f"Emp grade level={Emp.gradeLevel},RD={RD.gradeLevel},PM={PM.gradeLevel}")
PM.gradeLevel = 7
print(f"[II]Emp grade level={Emp.gradeLevel},RD={RD.gradeLevel},PM={PM.gradeLevel}")
Emp.gradeLevel = 8
print(f"[III]Emp grade level={Emp.gradeLevel},RD={RD.gradeLevel},PM={PM.gradeLevel}")
r1 = RD()
r1.startWork()
p1 = PM()
p1.startWork()