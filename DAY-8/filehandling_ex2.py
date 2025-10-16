#method to update content of file and make sure the file name exist


import os #(not necessarily need to import os anymore)
# filepath=r"C:\Users\Faridah\Desktop\AIML\Python Training\DAY-8\ourfiles\sample.txt"
filepath=os.getcwd()  #to get directory path
filename=input("Enter name to update File:\t")
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)):
    file=open(fullpath,"a")
    content=input("Enter text to write a file:\t")
    file.write(content)
    print(f"File {filename} create at {fullpath} and content saved in file")
    file.close()
else:
    print(f"No such file {filename} exist")