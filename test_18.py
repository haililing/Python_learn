import os

keyword = input("字符串")

for root,dirs,files in os.walk('.'):
    for file in files:
        if keyword in file:
            path = os.path.join(root,file)
            relpath = os.path.relpath(path,'.')
            print(relpath)