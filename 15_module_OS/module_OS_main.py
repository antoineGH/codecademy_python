import os
from datetime import datetime
from functions_module_OS import file_stat, path_desktop, count_items

### CODE ###

path = path_desktop()
os.chdir(path)

count_items(path)
list_item = os.listdir(path)

for item in list_item:
    file_stat(item)


