import os
def get_file_names(folder,file):
    lt= os.listdir(folder)
    with open(file, 'w') as f:
        for element in lt:
            f.write(element + '\n')

def get_all_file_names(folder):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    lt = os.listdir(folder)
    lt.reverse()
    for element in lt:
        print(element)

def print_line_one(folder):
    """takes a list of filenames and print the first line of each"""
    lt = os.listdir(folder)
    for element in lt:
        if '.csv'in element or '.txt' in element:
            with open(folder + '/' + element, 'r') as f:
                print(f.readline())
def print_emails(folder):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    lt = os.listdir(folder)
    for element in lt:
        if '@' in element:
            print(element)

def write_headlines(folder):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    lt = os.listdir(folder)
    for element in lt:
        if '.md' in element:
            with open(folder + '/' + element, 'r') as f:
                for line in f:
                    if '#' in line:
                        print(line)