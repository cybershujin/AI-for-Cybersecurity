## if you have not already imported os, uncomment the next line
#import os

def get_file_list(starting_directory="../data/file/path/filename"):
    final_list = list()
    files = os.listdir(starting_directory)
    for file in files:
        file_name = os.path.join(starting_directory, file)
        if os.path.isdir(file_name):
            final_list = final_list + get_file_list(file_name)
        else:
            final_list.append(file_name)
    return final_list

all_files = get_file_list()
print(len(all_files))
print(all_files[:5], all_files[-5:])
