import filecmp, shutil, os, sys

dir_list = [{'src':r'D:/src','dest':r'D:/dest'},];
IGNORE = []

def file_backup(src, dest):
    if os.path.isdir(src) and os.path.isdir(dest):
        dir_cmp = filecmp.dircmp(src, dest, ignore=IGNORE)

        # for items only in the dest directory, just remove it
        for item in dir_cmp.right_only:
            if os.path.isdir(dest+'/'+item):
                shutil.rmtree(dest+'/'+item)
            else:
                os.remove(dest+'/'+item)

        # for items only in the src directory, just copy it
        for item in dir_cmp.left_only:
            if os.path.isdir(src+'/'+item):
                shutil.copytree(src+'/'+item, dest+'/'+item)
            else:
                shutil.copy2(src+'/'+item, dest+'/'+item)

        # for items in common, for directories, sync them,
        # if they are files, do nothing if they are the same or copy it if not
        # For SPECIAL case: 
        for item in dir_cmp.common:
            if os.path.isdir(src+'/'+item) and os.path.isdir(dest+'/'+item):
                file_backup(src+'/'+item, dest+'/'+item)
            elif os.path.isdir(src+'/'+item) and os.path.isfile(dest+'/'+item):
                os.remove(dest+'/'+item)
                shutil.copytree(src+'/'+item, dest+'/'+item)
            elif os.path.isfile(src+'/'+item) and os.path.isdir(dest+'/'+item):
                shutil.rmtree(dest+'/'+item)
                shutil.copy2(src+'/'+item, dest+'/'+item)
            else:
                if isFileTheSame(src+'/'+item, dest+'/'+item):
                    pass
                else:
                    shutil.copy2(src+'/'+item, dest+'/'+item)
        return 
    else:
        print('You can only sync directorys')
        return

def isFileTheSame(fileA, fileB):
    if os.path.getsize(fileA) == os.path.getsize(fileB) and \
       os.path.getmtime(fileA) == os.path.getmtime(fileB):
        return True
    return False

if __name__ == '__main__':
    for directory in dir_list:
        file_backup(directory['src'], directory['dest'])
