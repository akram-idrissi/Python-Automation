import os


def set_dir(directory):
    os.chdir(directory)


def create_file(filename):
    if os.path.exists(filename):
        os.makedirs(filename)


def append_to_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data + '\n')


def clean_file(filename):
    with open(filename, 'w') as f:
        pass


def read_file(filename):
    data = set()
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.add(line.strip())
    data = list(data)
    return data


def modify_file(filename):
    data = []
    contents = read_file(filename)
    clean_file(filename)
    for content in contents:
        data.append(content.split("|")[0])
    for d in data:
        append_to_file(filename, d)
