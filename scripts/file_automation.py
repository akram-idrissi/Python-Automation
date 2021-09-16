import os

from glob import glob

number = 0
base_path = "C:/Users/Ce pc/Downloads"
os.chdir(base_path)


def extension(file_name):
    """ returns the name and extension of a file ."""
    name, ext = os.path.splitext(file_name)
    name_ = name.replace("C:/Users/Ce pc/Downloads\\", "")
    return name_, ext


def make_dir(ext):
    # creates a directory if it doesn't already exist.
    if not os.path.exists(ext) and ext != "":
        os.makedirs(ext)
        return True
    return False


def enum_max(ext):
    """ returns the index of the last file in the folder, 0 if it's empty """
    try:
        enum = clean_names(ext)
        enum_max = max(enum)
        return enum_max
    except:
        return 0


def clean_names(ext):
    names = glob(ext + "/*")
    clean_names = [name.replace(ext + "\\", "") for name in names]
    numbers = [int(name.split('-')[0]) for name in clean_names]
    return numbers


def move_files(name, ext, number):
    """ move the files from downloads folder to the given folder """
    full_name = name + ext
    number += 1
    new = str(number).zfill(2) + '-' + full_name
    os.rename(base_path + '/' + full_name, base_path + '/' + ext + '/' + new)


def move_folders(name, ext, number):
    """ move the folders from downloads folder to the given folder """
    full_name = name + ext
    number += 1
    new = str(number).zfill(2) + '-' + full_name
    os.rename(base_path + '/' + full_name, base_path + '/' + "folders" + '/' + new)


def if_delete(ext):
    """ when you delete a file """
    all_files = [name.replace(ext + "\\", "") for name in glob(ext + '/*')]
    lastFile_num = enum_max(ext)
    all_files_length = len(all_files)

    if (lastFile_num > 0) and (lastFile_num > all_files_length):

        l = list(range(1, all_files_length + 1))
        n = list(map(str, l))
        k = [i.zfill(2) for i in n]
        m = [file.split('-') for file in all_files]

        i = 0
        for name in m:
            new_name = k[i] + '-' + "".join(name[1:])
            i += 1
            os.rename(ext + '/' + '-'.join(name), ext + '/' + new_name)


print("We're Starting ...")
for filename in glob(base_path + '/*'):
    done = False
    name, ext = extension(filename)
    if ext == "" and "." not in name:
        if name == "folders":
            continue
        make_dir("folders")
        number = enum_max(ext)
        move_folders(name, ext, number)
        list(map(if_delete, os.listdir()))
        done = True

    make_dir(ext)
    number = enum_max(ext)
    try:
        move_files(name, ext, number)
    except PermissionError:
        pass

list(map(if_delete, os.listdir()))
print("it's done !!")
