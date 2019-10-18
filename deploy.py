import glob
import os
from zipfile import ZipFile
from zipfile import ZIP_DEFLATED
dir = os.path.dirname(__file__)
files = glob.glob(os.path.join(dir, 'CarPlacer', '[!__]*.py'))
files.remove(os.path.join(dir, 'CarPlacer', 'main.py'))
if not os.path.exists(os.path.join(dir, 'deploy')):
    os.makedirs((os.path.join(dir, 'deploy')))
deployedMain = open("deploy/main.py", "w+")
for file in files:
    f = open(file, "r")
    deployedMain.write(f.read());
    deployedMain.write("\n")
mainPath = os.path.join(dir, 'CarPlacer', 'main.py')
f = open(mainPath)
for line in f:
    if line == "#END\n":
        break
deployedMain.write("import sys \nf = sys.stdin \n")
deployedMain.write(f.read())
deployedMain.close()
with ZipFile('deploy/my_python_files.zip','w') as zip:
    zip.write(mainPath, os.path.realpath('deploy/main.py'), ZIP_DEFLATED)
os.remove(os.path.realpath('deploy/main.py'))
