import os
# FileNotFoundError, ValueError, TypeError


class FileAutomation:
    def __init__(self, path):
        self.path = path
        os.chdir(self.path)

    @staticmethod
    def set_directory(path):
        os.chdir(path)

    @staticmethod
    def get_extension(file_name):
        return os.path.splitext(file_name)

    @staticmethod
    def make_dir(directory):
        if not os.path.exists(directory) and directory:
            os.mkdir(directory)

    @staticmethod
    def get_files(directory):
        # path = os.path.join(self.path, directory)
        return os.listdir(directory)

    def get_index(self, directory):
        try:
            files = self.get_files(directory)
            indexes = [int(file_name.split("-")[0]) for file_name in files]
            last_index = max(indexes)
            return last_index
        except ValueError:
            return 0

    def move_files(self, name, extension, number):
        file_name = "".join([name, extension])
        number += 1
        new_file_name = "".join([str(number).zfill(2), "-", file_name])
        old_path = os.path.join(self.path, file_name)
        new_path = os.path.join(self.path, extension, new_file_name)
        os.rename(old_path, new_path)

    def move_folder(self, directory, number):
        number += 1
        new_file_name = "".join([str(number).zfill(2), "-", directory])
        old_path = os.path.join(self.path, directory)
        new_path = os.path.join(self.path, "Folders", new_file_name)
        os.rename(old_path, new_path)

    def if_delete(self, directory):
        files = self.get_files(directory)
        last_index = self.get_index(directory)
        total_files = len(files)

        if (last_index > 0) and (last_index > total_files):
            file_numbers = list(range(1, total_files + 1))
            to_string = list(map(str, file_numbers))
            two_digit_format = [i.zfill(2) for i in to_string]
            split_files = [f.split("-") for f in files]

            n = 0
            for name in split_files:
                new_name = "".join([two_digit_format[n], "-", "".join(name[1:])])
                n += 1
                old_path = "".join([directory, "/", "-".join(name)])
                new_path = "".join([directory, "/", new_name])

                os.rename(old_path, new_path)

    def run(self):
        for file_name in os.listdir():
            name, extension = self.get_extension(file_name)
            if "." in name and extension == "":
                continue

            if not extension and "." not in name and name != "Folders":
                self.make_dir("Folders")
                last_index = self.get_index("Folders")
                self.move_folder(name, last_index)
            if name and extension:
                # print(extension)
                self.make_dir(extension)
                last_index = self.get_index(extension)
                self.move_files(name, extension, last_index)
        list(map(self.if_delete, os.listdir()))


if __name__ == "__main__":
    files_path = r"C:\Users\Ce pc\Downloads"
    app = FileAutomation(files_path)
    app.run()
