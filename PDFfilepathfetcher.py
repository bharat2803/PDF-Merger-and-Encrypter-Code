import sqlite3
from PDFfilepathgenerator import generate
def fetchpath(filename):
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

if __name__ =="__main__":
    generate()
    print(fetchpath("Communication.pdf"))
