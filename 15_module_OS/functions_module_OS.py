import os
from datetime import datetime
from hurry.filesize import size

### FUNCTIONS ###

def path_desktop():
    path = os.path.join('C:\\Documents and Settings\\',os.getlogin(),'Desktop')
    return path

def count_items(path):
    nb_items = len(os.listdir(path))
    print("PATH \"{}\" HAS {} ITEMS.\n".format(path, nb_items))

def last_modified(file):
    mod_time = os.stat(file).st_mtime
    mod_time_stamp = datetime.fromtimestamp(mod_time)
    return mod_time_stamp

def recent_access(file):
    rec_time = os.stat(file).st_atime
    rec_time_stamp = datetime.fromtimestamp(rec_time)
    return rec_time_stamp

def get_size(file):
    file_size = os.stat(file).st_size
    file_size = size(file_size)
    return file_size

def get_owner_group(file):
    file_owner_id = os.stat(file).st_uid
    file_group_id = os.stat(file).st_gid
    return (file_owner_id, file_group_id)

def file_stat(file):
    # Get Information
    mod_time_stamp = last_modified(file)
    rec_time_stamp = recent_access(file)
    file_size = get_size(file)
    file_owner_id, file_group_id = get_owner_group(file)

    # Convert Timestamp
    mod_time_stamp = mod_time_stamp.strftime("%d/%m/%y %H:%M")
    rec_time_stamp = rec_time_stamp.strftime("%d/%m/%y %H:%M")

    # Display
    print("--- FILE {} ---".format(file))
    print("SIZE {}".format(file_size))
    print("OWNER {} GROUP {}".format(file_owner_id, file_group_id))
    print("LAST MODIFIED {}".format(mod_time_stamp))
    print("LAST ACCESSED {}\n".format(rec_time_stamp))

