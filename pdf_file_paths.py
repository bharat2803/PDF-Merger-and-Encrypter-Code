import sqlite3
import os
from pathlib import Path

#To create database which contains the list of all the PDFs and their paths present in the system
def generate():
    dbconnect = sqlite3.connect("pdfdatabase.sqlite")

    dbcursor = dbconnect.cursor()

    dbcursor.executescript("""
    DROP TABLE IF EXISTS PDFs;
    CREATE TABLE PDFs (filepath VARCHAR,
                    pdf_files VARCHAR);""")

    #This function is used for recursion to create the path of every PDF present in the system.
    def create_path(pathname):
        for x in os.scandir(pathname):
            if pathname == "C:\\Users\\":
                try:
                    if x.name not in ['All Users','Default','Default User']: #Restricted folders
                        if os.path.isdir(x):
                            nextpath= os.path.join(pathname,x.name+'\\')
                            create_path(nextpath)

                        if os.path.isfile(x):
                            if x.name.split('.')[-1] == "pdf":
                                filepath=os.path.join(pathname,x.name)
                                dbcursor.execute("INSERT INTO PDFs (filepath,pdf_files) VALUES (?,?)",(filepath,x.name,))
                except:
                    pass
            else:
                try:
                    if os.path.isdir(x):
                        nextpath= os.path.join(pathname,x.name+'\\')
                        create_path(nextpath)

                    if os.path.isfile(x):
                        if x.name.split('.')[-1] == "pdf":
                            filepath= os.path.join(pathname,x.name)
                            dbcursor.execute("INSERT INTO PDFs (filepath,pdf_files) VALUES (?,?)",(filepath,x.name,))
                except:
                    pass


    create_path("C:\\Users\\")
    dbconnect.commit()
    dbconnect.close()

#To get the filepath of the PDF given.
def fetch_path(filename):
        try:
            dbconnect = sqlite3.connect("pdfdatabase.sqlite")
            dbcursor = dbconnect.cursor()
            dbcursor.execute("SELECT filepath FROM PDFs WHERE pdf_files = ?",(filename,))
            filepaths = dbcursor.fetchall()
            l = len(filepaths)
            if l > 1:
                print(f"There are {l} {filename} files at different locations:\n")
                for i,filepath in enumerate(filepaths):
                    print(i+1,f") {filepath[0]}")
                while True:
                    choice=input("\n Please choose one of the above by entering the corresponding number. Enter exit to skip this file: ")
                    if choice == "exit":
                        return None
                    else:
                        try:
                            return filepaths[int(choice)-1][0]
                        except:
                            print("Please enter the valid choice.")
                            continue
            else:
                return filepaths[0][0]
        except:
            print("\n\nPDF not found. Please check the name of the file and try again.\n \n")
            return None

#To get list of all the PDF files present
def get_files_list():
    print("\n\n  These are all the PDF files present in your system: \n\n")
    dbconnect = sqlite3.connect("pdfdatabase.sqlite")
    dbcursor = dbconnect.cursor()
    dbcursor.execute("SELECT pdf_files FROM PDFs ORDER BY pdf_files")
    pdfs_list = dbcursor.fetchall()
    for i in range(len(pdfs_list)):
        print(str(i)+') '+pdfs_list[i][0])

if __name__ =="__main__":
    generate()
    print("Table created")
    get_files_list()
