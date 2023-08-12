import os

for dir_name, sub_dir_names, file_names in os.walk('..'):
    print(f'Current dir : {dir_name}')
    print(f'Sub directory : {sub_dir_names}')
    print(f'Filenames : {file_names}')