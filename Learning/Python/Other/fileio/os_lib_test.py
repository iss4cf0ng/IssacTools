import os

print(os.getcwd()) # Current path

print(os.path.abspath('.')) # Absolute path of .
print(os.path.abspath('..')) # Absolute path of ..
print(os.path.abspath('os_lib_test.py')) # Absolute path of this file

print(os.path.relpath('D:\\')) # relative path
try:
    print(os.path.relpath('C:\\')) # Error
except Exception as e:
    print(e)
