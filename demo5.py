#demo5

import math

radius1 = 2.0
area1 = radius1 * radius1 * math.pi

str1 = 'radius=%f,area=%f' % (radius1, area1)

str2 = 'radius=%.1f,area=%.2f' % (radius1, area1)

str3 = 'radius=%(r).1f,area=%(a).2f' % {'r': radius1, 'a': area1}

str4 = 'radius=%(r).1f,area=%(a).2f' % {'a': area1, 'r': radius1}

str5 = 'radius={},area={}'.format(radius1, area1)

str6 = 'radius={:.1f},area={:.2f}'.format(radius1, area1)

str7 = 'radius={0:.1f},area={1:.2f}'.format(radius1, area1)

str8 = 'radius={1:.1f},area={0:.2f}'.format(area1, radius1)

str9 = 'radius={r:.1f},area={a:.2f}'.format(r=radius1, a=area1)

str10 = f'radius={radius1},area={area1}'

str11 = f'radius={radius1:.1f},area={area1:.2f}'

print("str1="+str1)
print("str2="+str2)
print("str3="+str3)
print("str4="+str4)
print("str5="+str5)
print("str6="+str6)
print("str7="+str7)
print("str8="+str8)
print("str9="+str9)
print("str10="+str10)
print("str11="+str11)