import glob

files = glob.glob('?bc.txt')
print(files)


files = glob.glob('*.txt')
print(files)


files = glob.glob('*')
print(files)
