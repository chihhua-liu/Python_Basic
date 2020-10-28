##demo33
def func33(fix1, fix2, *args):
    print("fix part1=", fix1)
    print("fix part2=", fix2)
    for arg in args:
        print("variable part:", arg)


func33("Hello", "world")
func33("hihi", "welcome", "Sunday")
func33("hihi", "again", "Sunday", 'Monday', 'Tuesday')
func33(fix1="Hello", fix2="World")