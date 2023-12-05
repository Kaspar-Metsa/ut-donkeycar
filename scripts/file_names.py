import os

## script for renaming files in directory

directory = './STOP_MODEL/NOT_STOP_tub'

i = 1 ## number of the last file in directory + 1
for file_name in os.listdir(directory):
    old_name = os.path.join(directory, file_name)


    if os.path.isfile(old_name):
        extension = os.path.splitext(file_name)[1]
        new_name = os.path.join(directory, f'{i:05}{extension}')

        os.rename(old_name, new_name)
    i += 1
