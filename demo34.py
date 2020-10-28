#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#demo34

def func34(fix1, fix2, **kwargs):
    print(f"fix1={fix1}, fix2={fix2}")
    for k, v in kwargs.items():
        print(f"variable part key={k}, value={v}")


func34("first", "try")
func34(fix1="second", fix2="try")
func34(fix1="ucom", fix2="Remote", name="C++")
# func34(fix1="ucom", fix2="Taipei", name="BDPY", duration=35, instructor="MarkHo")
# func34("ucom", "Hsinchu", name="POOP", duration=35, instructor="MarkHo")
# d1 = {'name': 'Oracle9i', 'duration': '42hr', 'instructor': "Frank"}
# func34("Oracle", "certified", **d1)