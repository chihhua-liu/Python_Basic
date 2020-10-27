# demo6
class Foo(object):
    def __str__(self):
        return '使用[str]格式輸出'

    def __repr__(self):
        return '使用[repr]格式輸出'


f1 = Foo()
print(f1)
print(repr(f1))
print('%s,%r' % (f1, f1))
print('===>{0!s},{0!r},{0!a}'.format(f1))