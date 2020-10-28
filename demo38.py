# demo38    os and sys

import sys
import os
import time

# DIR1 = "working"
DIR1 = "工作目錄"
print(os.getcwd())   # 傳回工作目錄
os.mkdir(DIR1)       # 建目錄
os.chdir(DIR1)       # 進入目錄

print(os.getcwd())
time.sleep(5)
os.chdir('..')
os.rmdir(DIR1)
print(os.getcwd())
print(sys.argv)
print(sys.executable)
sys.exit(1)
