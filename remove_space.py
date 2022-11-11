import sys, os, click

path='./'
fileV = os.listdir(path)
# print(len(fileV), fileV)

fset = set()

for fn in fileV:
    if not ' - ' in fn:
        continue
    fieldV = fn.strip().split('-')
    # assert len(fieldV)==2, fn
    newV = []
    for term in fieldV:
        newV.append(term.strip())
    nameNew = '-'.join(newV)

    if not os.path.exists(nameNew):
        print('move %s to %s' % (fn , nameNew))
        if click.getchar() == 'y':
            os.rename(fn, nameNew)
    else:
        print(fn)
        if click.getchar() == 'y':
            os.remove(fn)
