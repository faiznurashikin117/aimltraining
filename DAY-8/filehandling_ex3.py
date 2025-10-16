#method to update content of file


import os #(not necessarily need to import os anymore)
# filepath=r"C:\Users\Faridah\Desktop\AIML\Python Training\DAY-8\ourfiles\sample.txt"
filepath=os.getcwd()  #to get directory path
filename=input("Enter name to update File:\t")
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)):
    file=open(fullpath,"r")         # 'r' to read content
    content=file.read()             #to read content
    print("File content as follows")
    print(content)
    file.close()
else:
    print(f"No such file {filename} exist")