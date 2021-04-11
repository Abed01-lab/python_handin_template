import csv
import argparse

def print_file_content(file):
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        for element in lst:
            f.write(element + "\n")


def write_strings_to_file(file, *strings):
    with open(file, 'w') as f:
        for string in strings:
            f.write(string + "\n")
            print(string)

            
def read_csv(input_file):
    with open(input_file) as f:
        new_list = []
        reader = csv.reader(f)
        for row in reader:
            new_list.append(row)
        return new_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that reads from csv and write to txt. the path is the location of the csv and file_name is the location of the file to write to.')
    parser.add_argument('path', help='The path to the csv file')
    parser.add_argument('-file', '--file_name', help='The file to write to')

    args = parser.parse_args()
    print('csv path:', args.path)
    print('file_name:', args.file_name)
    
    if args.file_name is not None:
        write_list_to_file(args.file_name, read_csv(args.path))