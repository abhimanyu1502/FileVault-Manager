from pathlib import Path
import os

# Set base directory to the folder containing this script
BASE_DIR = Path(__file__).resolve().parent

def createfile():
    try:
        name=input("Please tell your file name:- ")
        path = BASE_DIR / name
        if not path.exists():
            with open(path,"w") as f:
                data=input("Enter your data you want to write in your file: ")
                f.write(data)
            print(f"Your file is created successfully at: {path}")
        else:
            print("Error file already exists")
    except Exception as err:
        print(f"Error occurred as {err}")


def readfile():
    try:
        name=input("Please tell the file name you want to read :- ")
        path=BASE_DIR / name
        if path.exists():
            with open(path,"r") as f:
                content=f.read()
                print(f" Your file content is: \n{content}")
        else:
            print ("Error no such file found")
    except Exception as err:
        print(f"An error occurred as {err}")


def updatefile():
    try:
        name=input("Please enter the name of the file you want to update:- ")
        path=BASE_DIR / name
        if path.exists():
            print("Operations you can perform")
            print("Press 1 for renaming the file")
            print("Press 2 for Appending the content in the file")
            print("Press 3 for overwriting the file ")

            choice=int(input("Tell the operations you want to perform :- "))
            if choice==1:
                newname=input("enter the new name of your file :- ")
                newpath=BASE_DIR / newname
                if not newpath.exists():
                    path.rename(newpath)
                    print("File has been renamed successfully")
                else:
                    print (" error file already exists ")
            elif choice==2:
                with open(path,"a") as f:
                    data=input("Enter the data you want to append in the file :- ")
                    f.write("\n"+data)
                print("Data appended successfully")
            elif choice==3:
                with open(path,"w") as f:
                    data=input(" Enter the data you want to overwrite in the file :- ")
                    f.write(data)
                print("Data Overwritten successfully")
        else:
            print("Error file not found")
    except Exception as err:
        print(f" An error occurred as {err}")


def deletefile():
    try:
        name=input("enter the name of the file you want to delete :- ")
        path=BASE_DIR / name
        if path.exists():
            path.unlink()
            print(f" The file {name} has been deleted successfully")
        else:
            print("Error file not found ")
    except Exception as err:
        print (f"An error occurred as {err}")



print(" Press 1 for creating a file")
print(" Press 2 for reading a file")
print(" Press 3 for updating a file")
print(" Press 4 for deleting a file")

a=input("\n Tell your response:- ")
if a == "1":
    createfile()
elif a == "2":
    readfile()
elif a == "3":
    updatefile()
elif a == "4":
    deletefile()