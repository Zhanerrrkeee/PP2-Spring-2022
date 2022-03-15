import os
DIR = os.getcwd()
# print(DIR)
# for i in os.listdir(DIR):
#     print(os.path.join(DIR,i))  
# print(os.getcwd())
for i in os.listdir(DIR):
    target_path = os.path.join(DIR,i)
    if os.path.isdir(target_path):
        print(i)
        for j in os.listdir(target_path):
            target_path2 = os.path.join(target_path,j)
            if os.path.isfile(target_path2):
                print(f'----FILE: {j}')
