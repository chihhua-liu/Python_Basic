class Team:
    name = "Normal Team"


t1 = Team()
t2 = Team()
print(t1.name, t2.name, Team.name)
t1.name = 'Mobile R&D'               # 實例 can overwrite
print(t1.name, t2.name, Team.name)
Team.name = 'standard team'          # class can  overwrite ,but 實例 first 不會改變
print(t1.name, t2.name, Team.name)
del t1.name                          # del 實例屬性後。 實例屬性=class屬性
print(t1.name, t2.name, Team.name)
t1.size = 7
t2.location = 'Taichung'
print(t1.size, t1.name, t2.location, t2.name)