import os
import inspect
print("Current Directory",os.getcwd())
print("Login name:",os.getlogin())

# functions=inspect.getmembers(os,inspect.isbuiltin)

# print("All function in os module")
# for n,func in functions:
#     print(n,end="\t")


#create a folder inside current directory using Python program

import os
cdir=os.getcwd()   #currentDirectory
folder_name=input("Enter folder name to create:\t")
folder_path=os.path.join(cdir,folder_name) #to join the current directory path with the new folder name to make a full path
if(os.path.exists(folder_path)):
    print("Folder already exist")
else:
    os.makedirs(folder_path,exist_ok=True)
    print(f"{folder_name} created at {folder_path}")


#InClassExercise
#Rename a folder function
# os.rename(folder_name,"renamed_folder")

#write code to rename a folder
#you will take folderName from user 
#if it is exist, you will ask new name and rename it


#answer
import os
cdir=os.getcwd()
old_folder_name=input("Enter the existing folder name:\t")
if(os.path.exists(old_folder_name)):
    new_folder_name=input("Enter folder name to rename:\t")
    os.rename(old_folder_name,new_folder_name)
    print(f"Folder renamed as:{new_folder_name}")
else:
    print("Folder does not exists")










