# #Method 1 just add new file name manually in file path need to have r for reading purpose
# filepath=r"C:\Users\Faridah\Desktop\AIML\Python Training\DAY-8\ourfiles\sample.txt"
# file=open(filepath,"w")
# content=input("Enter text to write a file:\t")
# file.write(content)
# file.close()

# #Method 2  to create new file and write
# import os #(not necessarily need to import os anymore)
# filepath="C:\\Users\\Faridah\\Desktop\\AIML\\Python Training\\DAY-8\\ourfiles\\sample.txt"
# filename=input("Enter name to create File:\t")
# fullpath=os.path.join(filepath,filename)
# file=open(fullpath,"w")
# content=input("Enter text to write a file:\t")
# file.write(content)
# print(f"File {filename} create at {fullpath} and content saved in file")
# file.close()

# #Method 3 to create new file and write by import directory from os
# import os #(not necessarily need to import os anymore)
# # filepath=r"C:\Users\Faridah\Desktop\AIML\Python Training\DAY-8\ourfiles\sample.txt"
# filepath=os.getcwd()  #to get directory path
# filename=input("Enter name to create File:\t")
# fullpath=os.path.join(filepath,filename)
# file=open(fullpath,"w")
# content=input("Enter text to write a file:\t")
# file.write(content)
# print(f"File {filename} create at {fullpath} and content saved in file")
# file.close()

