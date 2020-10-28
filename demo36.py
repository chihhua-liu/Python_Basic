#demo36

def func36_employee_profile(id, name, role):
    print(f"employee id=[{id}], name=[{name}], role=[{role}]")
    pass


func36_employee_profile(id=1, name='Mark', role="Engineer")
d1 = {"id": 2, "name": "James"}
func36_employee_profile(**d1, role='FAE')
func36_employee_profile(role='FAE', **d1)
d2 = {"id": 3, "role": "Manager", "name": "Eric"}     # sequence can different
func36_employee_profile(**d2)