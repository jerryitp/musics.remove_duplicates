import sys, os

path='./Popular.Beyond/'
fileV = os.listdir(path)
# print(len(fileV), fileV)

fset = set()

for fn in fileV:
    fieldV = fn.strip().split('-')
    assert len(fieldV)==2, fieldV
    if fieldV[0] == 'BEYOND':
        fset.add(fn)
print(fset)

for fn in fileV:
    fieldV = fn.strip().split('-')
    assert len(fieldV)==2, fieldV
    if fieldV[0] == 'BEYOND':
        continue
    else:
        nameOld = fn
        nameNew = 'BEYOND-'+fieldV[1]
        ap = 1
        while nameNew in fset:
            print(fn, '-----------------')
            partV = fieldV[1].split('.')
            assert len(partV)==2
            nameNew = 'BEYOND-'+partV[0]+str(ap)+'.'+partV[1]
            ap += 1
        os.rename(path+nameOld, path+nameNew)
        print(nameOld, nameNew)
