from PIL import Image
import glob
import os
import tkinter as tk
from tkinter import filedialog


def compressImage(folder, path, reduce_by):
    image = Image.open(path)
    size = image.size

    new_size = (int(size[0] * reduce_by), int(size[1] * reduce_by))

    image = image.resize(new_size, Image.ANTIALIAS)
    new_path = path.replace(folder, folder + '/Compressed Images')
    final_path = new_path.replace('.JPG', '_Compressed.JPG')
    print(final_path)
    image.save(final_path, optimize=True, quality=95)

def main(*args, **kwargs):

    root = tk.Tk()
    root.withdraw()

    folder_selected = filedialog.askdirectory()
    images_dir = folder_selected + '\*.JPG'
    print(images_dir)
    images = glob.glob(images_dir)

    new_folder = folder_selected + '\Compressed Images'
    try:
        os.mkdir(new_folder)
    except OSError:
        print("Creation of the directory %s failed" % new_folder)
    else:
        print("Successfully created the directory %s " % new_folder)

    for i in range(0, len(images)):
        compressImage(folder_selected, images[i], 0.25)
    return 0

if __name__ == "__main__":
    main()
