import os
from datetime import datetime
from os import listdir
from os.path import isfile, join

### DECLARATIONS

download_dir = "E:\Downloads"
destination_dir = "E:\Images\Old\XHAMSTER"

### FUNCTIONS
def get_current_directory():
    current_directory = os.getcwd()
    return current_directory

def change_directory(dir_path):
    os.chdir(dir_path)

def input_username():
    username = input("Username: ")
    username_lower = username.lower()
    return username_lower

def create_directory(destination_dir, username):
    change_directory(destination_dir)
    if not os.path.exists(username):
        os.mkdir(username)
        print("\n--- CREATE DIR ---\n{}\n".format(destination_dir + "\\" + username))
    destination_dir_sub = destination_dir + "\\" + username
    return destination_dir_sub
                             
def set_new_title(file_name):
    new_title = file[22:-9] + ".mp4"
    new_title_lower = new_title.lower()
    return new_title_lower

def move_file(file, new_title, destination_dir_sub):
    origin = download_dir + "\\" + file
    destination = destination_dir_sub + "\\" + new_title
    print("--- MOVE ---\n{}\n>{}\n".format(origin, destination))
    os.replace(origin, destination)

### CALLS

# Create destination folder

username= input_username()
destination_dir_sub = create_directory(destination_dir, username)

# Get .mp4 files and format text

change_directory(download_dir)
current_directory = get_current_directory()

list_files = [file for file in listdir(current_directory) if isfile(join(current_directory, file))]

for file in list_files:
    if (".mp4" in file) and ("xhamster.com" in file):
            new_title = set_new_title(file)
            move_file(file, new_title, destination_dir_sub)
            

