#demo7
x1 = 30000
print('x1={0:d}/{0:} in decimal, {0:b} in binary'.format(x1))
print('x1={0:o} in octal, {0:x} in hexadecimal'.format(x1))

print('%10s' % '0123456789')
print('%10s' % '0123456789' * 2)
print()
print('%10s' % '0123456789'[:5])
print('%-10s' % '0123456789'[:5])
print('%10s' % '中文')
print()
print('{:10}'.format('0123456789'[:5]))   # default left
print('{:>10}'.format('0123456789'[:5]))  # > right
print('{:<10}'.format('0123456789'[:5]))  # left
print()
x2 = 23
print('x1={0:b}, in binary'.format(x2))
print('x1={0:8b}, in binary'.format(x2))