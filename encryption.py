import PyPDF2
import getpass
import os
import pdf_file_paths as pdf

def encrypt_pdf(filepath):   
    head,tail=os.path.split(filepath)
    with open(filepath, mode='rb') as file:
        file_to_encrypt=PyPDF2.PdfFileReader(file)
        if file_to_encrypt.isEncrypted:
            print("\n This file is already encrypted. If you want to decrypt the file or if you want to change the password of the file, choose the appropraite option from the menu.")
            return 0
        else:
            while True:
                password=getpass.getpass("Enter the new Password: ")
                confirmation=getpass.getpass("Confirm Password: ")
                if confirmation == password:
                    break
                else:
                    print("Password doesn't match. Please try again.")
            writer=PyPDF2.PdfFileWriter()
            writer.cloneReaderDocumentRoot(file_to_encrypt)
            writer.encrypt(password)
            with open(head+"\\clone.pdf", mode='wb') as file:
                writer.write(file)
    if os.path.exists(head+"\\temp.pdf"):
        os.remove(head+"\\temp.pdf")
    os.rename(filepath,head+"\\temp.pdf")
    os.rename(head+"\\clone.pdf",filepath)
    os.remove(head+"\\temp.pdf")
    os.startfile(filepath)

if __name__ == "__main__":
    encrypt_pdf(pdf.fetch_path("Resume.pdf"))
