import os

def rename_files():
    file_list = os.listdir(r'C:\Users\DAMMY\Documents\Python Scripts\tutorial_udacity\prank\prank')
    print(file_list)
    for file_name in file_list:
        saved_dir = os.getcwd()
        table = {ord(char):None for char in "1234567890"}
        os.chdir(r'C:\Users\DAMMY\Documents\Python Scripts\tutorial_udacity\prank\prank')
        os.rename(file_name,file_name.translate(table))
    os.chdir(saved_dir)
rename_files()