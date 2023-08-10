import contextlib
import sys
import os
import time
import requests
import threading
import queue

FILTERED = ['.jpg', '.png', '.gif', '.css']
TARGET = 'https://www.usj.edu.mo/'
THREAD = 10

answers = queue.Queue()
web_paths = queue.Queue()

def gather_path():
    for root, _, files in os.walk('.'):
        for filename in files:
            if os.path.split(filename)[1] in FILTERED:
                continue
            path = os.path.join(root, filename)
            if path.startswith('.'):
                path = path[1:]
            print(path)
            web_paths.put(path)

@contextlib.contextmanager
def chdir(path):
    this_dir = os.getcwd()
    os.chdir(path=path)
    try:
        yield
    finally:
        os.chdir(this_dir)

if __name__ == '__main__':
    with chdir('/'):
        gather_path()
    input("Press return to continue.")