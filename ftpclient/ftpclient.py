from ftplib import FTP

host = input("Please Enter the host: ")
user = input("Username: ")
password = input("Password: ")

with FTP(host) as ftp:
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())