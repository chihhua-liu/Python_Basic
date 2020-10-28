# demo31
def foo(a, b):
    return "[foo]result=" + str(a + b)


def bar(a, b):
    return "[bar]result=" + str(a * b)

if __name__ == '__main__':
    print("inside demo31:")
    print(foo(1, 2))
    print(bar(3, 4))