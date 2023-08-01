from ftplib import FTP

host = input("Please Enter the host: ")
user = input("Username: ")
password = input("Password: ")

def main():
    with FTP(host) as ftp:
        ftp.login(user=user, passwd=password)
        print(ftp.getwelcome())
        print("\n Welcome to ftpclient, programmed by mr.wipp\n")
        option = input("Please type a number: \n 1. Upload file\n 2. Retrieve File\n")
        if int(option) == 1:
            upload_file()
        elif int(option) == 2:
            retrieve_file()
        else:
            ("\nPlease choose a valid option!")
            exit()
def retrieve_file():
    localfil = input("\nPlease type the full file path you want the retrieved data be saved in: ")
    remotefil = input("\nPlease type the full file path of the file you want to retrieve: ")
    with open(localfil, 'wb') as f:
        FTP.retrbinary('RETR ' + remotefil, f.write, 1024)
    FTP.quit()

def upload_file():
    localfil = input("\nPlease type the full file path you want to upload: ")
    remotefil = input("\nSave uploaded file as: ")
    with open(localfil, 'rb') as f:
        FTP.storbinary('STOR ' + remotefil, f)
    FTP.quit()