# demo8
str1 = '0123456789'
print('%-10s<----' % str1)
print('%*s<----' % (-10, str1))
print('%-10s<----' % str1[:5])
print('%*s<----' % (-10, str1[:5]))
print('{:{}s}<----'.format(str1, 10))
print('{:{}s}<----'.format(str1[:5], 10))
print('{:<{}s}<----'.format(str1[:5], 10))
print('{:>{}s}<----'.format(str1[:5], 10))
print("----------------------------------------")
str2 = '測試'
print('{:_<10}'.format(str2))
print('{:*>10}'.format(str2))
print('{:!^10}'.format(str2))
str3 = str1 * 3
print('--%.6s--' % str3)
print('++{:.6s}++'.format(str3) )