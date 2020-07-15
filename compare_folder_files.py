import os
import filecmp
import shutil

def folder_diff(path1,path2):
    folder1 = os.listdir(path1) 
    folder2 = os.listdir(path2)
    same = 0
    diff = 0 
    for item1 in folder1:
        for item2 in folder2:
            if(item1==item2):
                try:
                    if (filecmp.cmp(path1+'/'+item1, path2+'/'+item2)):
                        same = same+1
                    else:
                        print('different',item1,' will be copied in folder')
                        diff = diff + 1
                        shutil.copy2(path1+'/'+item1, 'copied/')

                    pass
                except :
                    print(item1,'err')
                    pass

    print('rpt: same files ',same,' diff files',diff)
					


if __name__ == "__main__":
    src = 'C:/src'
    dst = 'C:/dst'
    folder_diff(src,dst)
   # print(data)