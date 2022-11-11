import sys, os, click

fExist = True
while fExist:
    fExist = False

    path='./'
    fileV = os.listdir(path)
    print(len(fileV), fileV)

    fset = set()
    idxV = [str(i) for i in range(1,9)]
    print(idxV)

    for fn in fileV:
        if fn in ['.DS_Store']:
            continue
        fieldV = fn.strip().split('.')
        # assert len(fieldV)==2, fieldV
        old_name = '.'.join(fieldV[:-1])
        app_name = fieldV[-1]
        assert app_name in ['flac', 'mp3', 'ogg', 'mflac', 'qmcflac', 'qmc0', 'mgg', 'mggl', 'mflach'], app_name
        assert len(old_name)>2

        if old_name[-2] == '-' and old_name[-1] in idxV:
            new_name = old_name[:-2]+'.'+app_name
            old_size = os.stat(path+fn).st_size
            fExist = True
            if not new_name in fileV:
                print('rename from %s of size %d to %s (not existed)' % (path+fn, old_size,path+new_name))
                if True: #click.getchar() == 'y':
                    os.rename(path+fn, path+new_name)
                    fileV.append(new_name)  
            else:
                new_size = os.stat(path+new_name).st_size
                # print(path+fn, old_size,'\n',path+new_name,new_size)
                if new_size>old_size:
                    print('removing %s of size %d and keep %s of size %d' % (path+fn, old_size, new_name, new_size,))
                    if click.getchar() == 'y':
                        os.remove(path+fn)
                elif new_size == old_size:
                    print('same: %s of size %d = %s of size %d(to remove)' % (new_name, new_size,path+fn, old_size))
                    if True: #click.getchar() == 'y':
                        os.remove(path+fn)
                else:
                    print('replacing %s of size %d (to remove) by %s of size %d' % (path+new_name,new_size, path+fn, old_size))
                    if click.getchar() == 'y':                
                        os.remove(path+new_name)
                        os.rename(path+fn, path+new_name)


            
