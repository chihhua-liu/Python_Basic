# demo35

def func35(fix1, fix2, fix3):
    print(f"fix1={fix1},fix2={fix2}, fix3={fix3}")


func35(1, 3, 5)
func35(fix1=1, fix2=3, fix3=5)
l1 = [2, 4, 6]      # * used list
func35(*l1)
l2 = [300, 500]
func35(100, *l2)
func35(*l2, 500)
d1 = {'name': 'Mark', 'role': "Engineer", 'level': 'Senior'}
func35(*d1)     #  * u數必須對其sed dictionary  (參