import shutil
import os

dumpdir = '/home/tibix/android/system_dumps/coreprimevelte/dump'
propdir = '../../../vendor/samsung/coreprimevelte/proprietary'

files = open('proprietary-files.txt').read().split('\n')
missing = []

for file in files:
    if not(file.startswith('#') or file == ""):
        if '|' in file:
            file = file.split('|')[0]
        if file.startswith('-'):
            file = file[1:]
        filedir = file[0:-(len(file.split('/')[-1]) + 1)]
        if not os.path.exists(f"{propdir}/{filedir}"):
            print(f"Creating direcotry {propdir}/{filedir}")
            os.makedirs(f'{propdir}/{filedir}')    
        if os.path.exists(f"{dumpdir}/{file}"):
            print(f"Copying {file}")
            shutil.copyfile(f"{dumpdir}/{file}",f"{propdir}/{file}")
        else:
            print(f"No such file: {file}")
            missing.append(file)

for file in missing:
    print(f"Missing: {file}")

print("extract-files.py done \nhere comes makefiles")
os.system('python3 setup-makefiles.py')
