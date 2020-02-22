
import os
from datetime import datetime

##print(dir(os))
print(dir(os))

#print(os.getcwd())

## Change directory 
#os.chdir("E:\git")

## Get User Login
#os.getlogin()

## Print current directory
#print(os.getcwd())

## Print list directories within path 
#print(os.listdir("E:\git\codeacademy_python"))

## Print list directories current directory
#print(os.listdir())

## Make directory
#os.mkdir("test_directory")

## Make directories in recursive way (deep levels)
#os.makedirs("test_directory\sub_test_directory\sub_sub_test_directory")

## Remove Single directory full path
#os.rmdir("test_directory\sub_test_directory\sub_sub_test_directory")

## Remove Recursive directory full path
#os.removedirs("test_directory\sub_test_directory")

## Create Folder
#os.mkdir("test")

## Create File
fo = open("text3.txt", "wb")
fo.close()

## Rename File (source to destination)
#os.rename("test.txt", "text2.txt")
#os.rename("text2.txt", "text3.txt")

## Rename Directory (source to destination)
#os.rename("test", "test2")

#st_mode: It represents file type and file mode bits (permissions).
#st_ino: It represents the inode number on Unix and the file index on Windows platform.
#st_dev: It represents the identifier of the device on which this file resides.
#st_nlink: It represents the number of hard links.
#st_uid: It represents the user identifier of the file owner.
#st_gid: It represents the group identifier of the file owner.
#st_size: It represents the size of the file in bytes.
#st_atime: It represents the time of most recent access. It is expressed in seconds.
#st_mtime: It represents the time of most recent content modification. It is expressed in seconds.
#st_ctime: It represents the time of most recent metadata change on Unix and creation time on Windows. It is expressed in seconds.
#st_atime_ns: It is same as st_atime but the time is expressed in nanoseconds as an integer.
#st_mtime_ns: It is same as st_mtime but the time is expressed in nanoseconds as an integer.
#st_ctime_ns: It is same as st_ctime but the time is expressed in nanoseconds as an integer.
#st_blocks: It represents the number of 512-byte blocks allocated for file.
#st_rdev: It represents the type of device, if an inode device.
#st_flags: It represents the user defined flags for file.

#print(os.stat("text3.txt"))
#print(os.stat("text3.txt").st_size)

# Store in mtime_text3 st_mtime of text3.txt
mtime_text3 = os.stat("text3.txt").st_mtime

# Convert it in human readable timestamp
print(datetime.fromtimestamp(mtime_text3))

#for dirpath, dirnames, filenames in os.walk("E:\git"):
#    print('CP: ', dirpath)
#    print('Directories: ', dirnames)
#    print('Files: ', filenames)
#    print()

##print(os.environ.get('HOME'))
#print(os.getcwd())
#os.chdir("E:\git")
#print(os.getcwd())

## Open file get the stream (all lines with .readlines and store it in file, iterate in file to get line by line
#with open("text3.txt", 'r') as f:
#    file = f.readlines()
#    for line in file:
#        print(line)

## Return a tupple (head tail)
#print(os.path.split('E:\git\text3.txt'))
#print(os.path.dirname('E:\git\text3.txt'))
#print(os.path.basename('E:\git\text3.txt'))

## Check if path exists
#print(os.path.exists('E:\git'))
#print(os.path.exists('E:\lolo'))

## Check if dir
#print(os.path.isdir('E:\git'))
#print(os.path.isdir('E:\git\text3.txt'))

## Check if file
#print(os.path.isfile('E:\git'))
#print(os.path.isfile('E:\git\text3.txt'))

# Split file name and file extension 
#tuple_fileext = os.path.splitext("E:\git\text3.txt")

## Split file name and file extension + change extension
#print(type(os.getcwd()))
#print(os.listdir(os.getcwd()))
#tuple_fileext = os.path.splitext("E:\git\text3.txt")
#print(tuple_fileext)
#path, ext = tuple_fileext
#print(path, ext)
#print(ext)
#print(type(ext))
#new_ext = ext.replace(ext, "doc")
#print(new_ext)
#print(path+'.'+new_ext)

