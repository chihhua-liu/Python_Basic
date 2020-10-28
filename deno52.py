# 手動建data目錄
# 手動建Python_Introduction
file1 = open('data/Python_Introduction', encoding='utf8')
print(type(file1))
readme_txt = file1.read()
print(type(readme_txt))
print(readme_txt[:50])
file1.close()

with open('data/Python_Introduction', encoding='utf8') as file2:
    print(type(file2))
    readme_txt2 = file2.read()
    print(type(readme_txt2))
    print(readme_txt2[:50])
# w/a
file3 = open('data/clone1', 'w', encoding='utf8')
file3.write(readme_txt)
file3.close()
# w/a
with open('data/clone2', 'a', encoding='utf8') as file4:
    file4.write(readme_txt2)