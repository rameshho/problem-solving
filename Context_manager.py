__author__ = 'rameshho'

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

#The below File will invoke class File and return the file handle
with File("D:\Python\programs\license.txt", 'r') as f:
    print(f.read())