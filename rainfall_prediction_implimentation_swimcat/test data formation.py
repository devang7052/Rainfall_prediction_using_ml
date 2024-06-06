import os
import shutil

# shutil.copytree("Swimcat","Swimcat_test")

# def clear_folder(folder_path_1):
#     # Check if the folder exists
#     if os.path.exists(folder_path_1):
#         for folder_path in os.listdir(folder_path_1):
#                 item_path_1 = os.path.join(folder_path_1, folder_path)

#                 for item in os.listdir(item_path_1):
#                     item_path = os.path.join(item_path_1, item)
#                     # Check if the item is a file
#                     if os.path.isfile(item_path):
#                         # Remove the file
#                         os.remove(item_path)
# clear_folder('Swimcat_test')



for i in os.listdir('Swimcat'):
    list2=os.listdir(f'Swimcat/{i}')
    num=0
    for j in list2:
        shutil.move(f'Swimcat/{i}/{j}',f'Swimcat_test/{i}/{j}')
        if num==50:
            break
        num +=1