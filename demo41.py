demo41
# manually make a directory working1
# copy demo1.py, demo2.py inside
import shutil

shutil.copytree('working1', 'working2')
shutil.rmtree('working1')
shutil.rmtree('working2')