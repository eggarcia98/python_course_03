''' 
You work at a company that receives daily data files from external partners. 
These files need to be processed and analyzed, but first, they need to be transferred to the company's internal network.

The goal of this project is to automate the process of transferring the files from an external FTP server 
to the company's internal network.

Here are the steps you can take to automate this process:
    
    1. Use the ftplib library to connect to the external FTP server and list the files in the directory.
    2. Use the os library to check for the existence of a local directory where the files will be stored.
    3. Use a for loop to iterate through the files on the FTP server and download them to the local directory 
    using the ftplib.retrbinary() method.
    4. Use the shutil library to move the files from the local directory to the internal network.
    5. Use the schedule library to schedule the script to run daily at a specific time.

    * You can also set up a log file to keep track of the files that have been transferred and any errors that 
    may have occurred during the transfer process.
'''

from ftplib import FTP
import os

host = "ftp.dlptest.com"
user = "dlpuser"
password = "rNrKYTX9g7z3RgJRmxWuGHbeu"

root_files = "./ftp_files_downloaded"
local_files = []
files_to_download = []


def recursive_files_looker(path_to_look):    
    for path in os.listdir(path_to_look):
        if os.path.isdir(os.path.join(path_to_look, path)):
            recursive_files_looker(f"{path_to_look}/{path}")
        else:
            file_path_witout_root_folder =  f"{path_to_look}/{path}".replace(root_files,".")
            local_files.append(file_path_witout_root_folder)

def get_server_files_path_list(local_files, server_directory_to_process = "/"):
    ftp.cwd(server_directory_to_process)
    current_directory = fr"{ftp.pwd()}"
    
    file_list = []
    ftp.retrlines('LIST', file_list.append)

    # print("\n".join(file_list))
    print("  - Looking directory:", server_directory_to_process)
    for line in file_list:
        name = line.split(None,8)[-1]
        if(line[0] == 'd'):
            # line = drwxr-xr-x    3 1001     1001           18 Jun 11 01:00 Vorne
            folder_path = f"{current_directory}/{name}".replace("//", "/")
            get_server_files_path_list(local_files, rf"{folder_path}")
        else:
            file_to_download = f"{current_directory}/{name}".replace("//", "/")
            if(f"./{file_to_download}" not in local_files):
                print(f"    + New File Found: {name}")
                files_to_download.append(file_to_download)
            

print("\n===== Getting Local Files =====")
recursive_files_looker(root_files)
print("  - "+"\n  - ".join(local_files))

with FTP(host) as ftp:
    ftp.login(user, password)
    try:
        print("\n===== Getting Server Path Files =====")
        get_server_files_path_list(local_files)
    except Exception as e:
        print("Error - Getting Server Path Files: ", e)

    print("\n===== Download Server Files =====")
    for file_to_download in files_to_download:
        print("  - Downloading... ", file_to_download)
        
        server_file_path = "/".join(file_to_download.split("/")[0:-1])
        server_file_name = file_to_download.split("/")[-1]

        local_file_path = root_files + server_file_path
        local_file_destination = f"{local_file_path}/{server_file_name}"

        try: 
            os.makedirs(local_file_path, exist_ok=True)
        except OSError as error: 
            print("Error creating directory locally: ",error)    

        file_to_download = file_to_download.replace("//", "/")
        try:
            ftp.retrbinary("RETR " + file_to_download ,open(local_file_destination, 'wb').write)
            print("   + Saved as ", local_file_destination)
        except Exception as e:
            ftp.quit()
            ftp.login(user, password)
            print(f"Error saving: \n{e}")
            
    ftp.quit()
