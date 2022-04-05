from ftplib import *
class App:
    def __init__(self):
        self.site_address = "speedtest.tele2.net"
        self.site_user = "anonymous"
        self.site_password = "anonymous"
        question = input("Do you want upload or download files? ")

        if "upload" in question.lower():
            self.upload()
        elif "download" in question.lower():
            self.download()
        else:
            print("Unexpected Error, Try Again")
            App()



    def download(self):
        with FTP(self.site_address) as ftp:
            ftp.login()
            print(ftp.getwelcome())
            print('Current Directory', ftp.pwd())
            ftp.dir()
            want_go_into_directory = input("Do you want to change directory? Yes/No ")
            if "yes" in want_go_into_directory.lower():
                next_dir = input("Where do you want to go next? ")
                ftp.cwd(next_dir)
                ftp.dir()
                try:
                    download = input("What file would you like to download? ")
                    ftp.retrbinary("RETR" + download, open(download, 'wb').write)
                    print("File download successfully")
                    print("Goodbye")
                except:
                    print("Error")

            elif "no" in want_go_into_directory.lower():
                try:
                    download = input("What file would you like to download? ")
                    ftp.retrbinary('RETR ' + download, open(download, 'wb').write)
                    print("File download successfully")
                    print("Goodbye")
                except:
                    print("Error")
            else:
                print("Unexpected Error")
            ftp.quit()

    def upload(self):
        with FTP(self.site_address) as ftp:
            ftp = ftp
            ftp.login()
            print(ftp.getwelcome())
            print('Current Directory', ftp.pwd())
            ftp.dir()
            question = input("Do you want to upload files here? ")

            if "no" in question.lower():
                next_dir = input("Where do you want to go next? ")
                ftp.cwd(next_dir)
                ftp.dir()
                name = input("Enter the name of the file you want to upload: ")
                with open(name, "rb") as file:
                    ftp.storbinary("STOR " + name, file)
                print("File uploaded succesfully")
                print(ftp.dir())

            elif "yes" in question.lower():
                name = input("Enter the name of the file you want to upload: ")
                with open(name, "rb") as file:
                    ftp.storbinary("STOR " + name, file)
                print("File uploaded succesfully")
                print(ftp.dir())

            else:
                 print("Unexpected Error")


            ftp.quit()



App()