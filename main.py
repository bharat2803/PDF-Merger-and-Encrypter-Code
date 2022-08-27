import os
from time import sleep
from encryption import encrypt_pdf
import decryption
from pdf_merger import pdf_merger
import pdf_file_paths as pdf

if __name__ == "__main__":

    os.system("cls")
    print("Loading... Creating list of PDFs")
    pdf.generate()      #To create database which contains list of all the PDFs and their path presnt in the system.
    clr = os.system("cls")
    sleep(0.75)
    print("\t \t \t \t\t\tPDF EDITING SOFTWARE \n \n \n\n\n\n")
    sleep(0.5)
    print("""\tWelcome to the PDF editing software. It allows you to encrypt, decryt and even merge of PDF files.
    \t   \tMoreover, you can even change the password of your already encrypted file \n \n\n""")
    print("Kindly choose one of the options below:\n\n")
    print("""1. View list of all PDFs present in your system.
2. Encrypt your pdf.
3. Decrypt your pdf.
4. Merge your pdfs.
5. Change the password of your pdf.
6. Exit\n \n""")

    while True:

        choice = input("\nEnter your choice=")
        try:
            if int(choice) not in [1, 2, 3, 4, 5, 6]:
                print("Please enter a valid choice.")
                continue
            else:
                choice = int(choice)
        except ValueError:
            print("Please Enter a Number.")
            continue
        if choice == 1:
            pdf.get_files_list() #To get the list of all PDFs presnt in the system.
        elif choice == 2:
            while True:
                file_to_encrypt = input("Enter the name of the PDF file to be encrypted: ")
                filepath = pdf.fetch_path(file_to_encrypt+".pdf")
                if filepath == None:
                    continue
                else:
                    status=encrypt_pdf(filepath)
                    if status != 0:
                        print("File encrypted. Opening you encrypted file.")
                        sleep(5)
                    break
        elif choice == 3:
            while True:
                file_to_decrypt = input("Enter the name of the PDF file to be decrypted: ")
                filepath = pdf.fetch_path(file_to_decrypt+".pdf")
                if filepath == None:
                    continue
                else:
                    decryption.decrypt_pdf(filepath)
                    print("File decrypted.")
                    break
        elif choice == 4:
            no_of_files = input("\n Enter the number of pdf files to be merged: ")
            filepaths=list()
            print("\n Now, enter the name of pdf files in the order in which they are to be merged: \n")
            for i in range(int(no_of_files)):
                while True:
                    filename=input(str(i+1)+") ") 
                    filepath = pdf.fetch_path(filename+".pdf")
                    if filepath == None:
                        continue
                    else:
                        filepaths.append(filepath)
                        break
            pdf_merger(filepaths)
        elif choice == 5:
            while True:
                filename = input("Enter the PDF file name: ")
                filepath = pdf.fetch_path(filename+".pdf")
                if filepath == None:
                    continue
                else:
                    decryption.decrypt_pdf(filepath)
                    status = encrypt_pdf(filepath)
                    print("Password changed successfully.")
                    break
        elif choice == 6:
            print("\n\tThank you for using this software. Wish you a great day ahead!")
            sleep(5)
            exit()
        cont=input("\n \nDo you want to continue?(y/n) ")
        while True:
            if cont == 'n':
                print("\n\tThank you for using this software. Wish you a great day ahead!")
                sleep(5)
                exit()
            elif cont == 'y':
                break
            else:
                cont = input("\n Please enter either y or n: ")
                continue
