import PyPDF2
from pikepdf import Pdf
from getpass import getpass
import os
import pdf_file_paths as pdf

#To open the encrypted file and create its clone named temp.pdf.
def decryption(filepath):
    with open(filepath, mode='rb') as file:
        decryption=PyPDF2.PdfFileReader(file)
        while True:
            password=getpass("Please Enter the Password: ")
            key=decryption.decrypt(password)
            if key == 0:
                print("Incorrect Password. Please try again.")
                #return key
            else:
                with Pdf.open(filepath, password=password) as temp:
                    temp.save("temp.pdf")
                return None

#To decrypt PDF
def decrypt_pdf(filepath):
    head,tail = os.path.split(filepath) #tail contains the filename and head contains the rest of the path
    with open(filepath, mode='rb') as file:
        decrypt_file=PyPDF2.PdfFileReader(file)
        if decrypt_file.isEncrypted:
            while True:
                password=getpass("Please Enter the Password: ")
                key=decrypt_file.decrypt(password)
                if key == 0:
                    print("Incorrect Password. Please try again.")
                else:
                    with Pdf.open(filepath, password=password) as temp:
                        temp.save(head+"\\decrypted.pdf")
                    break
        else:
            print("This file is not encrypted.")
            return
    os.remove(filepath)
    os.rename(head+"\\decrypted.pdf",filepath)
    os.startfile(filepath)

#To delete all the data presnt in temp.pdf
def blank_temp():
    with Pdf.open("temp.pdf",allow_overwriting_input=True) as file:
        del file.pages[:]
        file.save("temp.pdf")


if __name__ =="__main__":
    decrypt_pdf(pdf.fetch_path("Resume.pdf"))
