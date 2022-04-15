from PIL import Image
import getpass
import os

import view

def resize_pictures():
    current_username = getpass.getuser()

    filedir = os.listdir(r'\Users\{}\Pictures'.format(current_username))

    for filename in filedir:
        if entry_filename in filename:
            filepath = r'\Users\{}\Pictures\{}'.format(current_username, filename)
            img = Image.open(filepath)
            img.thumbnail((entry_resolution, entry_resolution))
            img.save(filepath)

def run():
    global entry_filename, entry_resolution
    entry_filename, entry_resolution = view.get_values()
    entry_resolution = int(entry_resolution)
    resize_pictures()

if __name__ == '__main__':
    run()