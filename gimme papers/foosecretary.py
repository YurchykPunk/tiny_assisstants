def where_is_parker(source, destination):
    import shutil
    import os
    import re

    copy_target = source
    paste_target = re.escape(destination)

    try:
        os.mkdir(paste_target)
    except:
        ...

    jail = []

    list_files = os.listdir(copy_target)

    with open('need.txt', 'r') as file:
        for line in file:
            for occ in list_files:
                if line.rstrip() in occ:
                    target_victim = f'{copy_target}/{occ}'
                    jail.append(occ)

                    
    for x in jail:
    #    print(x)
        shutil.copy(f'{copy_target}/{x}', f'{paste_target}/{x}')
