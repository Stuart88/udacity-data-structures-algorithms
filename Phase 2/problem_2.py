

'''
Recursively appends relevant file paths to array of strings.
Complexity: O(n), where n is the number of existing directories and files
'''

from genericpath import isdir, isfile
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
test_dir_path = f'{dir_path}\\testdir';


def find_files(suffix, path):

    if suffix is None or path is None:
        return []

    # Check path exists
    if os.path.isdir(path) == False and os.path.isfile(path) == False:
        return [] 

    directory = os.listdir(path)
    
    temp_arr = []

    # Check directory contains anything
    if len(directory) == 0:
        return []

    for p in directory:
        sub_path = os.path.join(path, p)
        if os.path.isdir(sub_path):
            temp_arr += find_files(suffix, sub_path) # <---- Recursion here.
        if os.path.isfile(sub_path) and p.endswith(suffix):
            temp_arr.append(sub_path) 
    
    return temp_arr




def test_for_suffix(test_name, suffix):
    passed = True
    for i in files:
        if not i.endswith(suffix):
            passed = False
    if passed:
        print(f'{test_name} Passed')
    else:
        print(f'{test_name} Failed')

def print_result(file_list):
    print('Found data:')
    if len(file_list) == 0:
        print('None')
    for i in file_list:
        print(i.replace(dir_path, '').replace('\\', '/')) # <-- uses string.replace() to help tidy the final result
    print()


files = find_files('.c', test_dir_path)
test_for_suffix('Test 1', '.c')
print_result(files)
print()


files = find_files('.h', test_dir_path)
test_for_suffix('Test 2', '.h')
print_result(files)

# Test null suffix
files = find_files(None, 123)
test_for_suffix('Test 3', 123)
print_result(files)

# Test null path
files = find_files('.c', None)
test_for_suffix('Test 4', None)
print_result(files)

# Test file type without any existing data
files = find_files('.exe', test_dir_path)
test_for_suffix('Test 5', '.exe')
print_result(files)


# Test empty string suffix
# Question: This results in getting all files. 
# It needs to be determined whether this is expected or an exception
files = find_files('', test_dir_path)
test_for_suffix('Test 6', '')
print_result(files)

# Test empty string path
files = find_files('.c', '')
test_for_suffix('Test 7', '')
print_result(files)





