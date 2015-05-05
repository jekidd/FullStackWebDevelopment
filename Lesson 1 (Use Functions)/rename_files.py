import os

def rename_files():
    #Get file names from folder
    file_list = os.listdir(r"C:\Users\jordan\code\Full Stack Web Development\Lesson 1 (Use Functions)\prank")

    #Change directory
    current_path = os.getcwd()
    os.chdir(r"C:\Users\jordan\code\Full Stack Web Development\Lesson 1 (Use Functions)\prank")

    #For each file, rename file
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

    #Change directory
    os.chdir(current_path)

rename_files()