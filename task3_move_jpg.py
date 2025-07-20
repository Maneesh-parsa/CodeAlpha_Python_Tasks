import os
import shutil

def move_jpg_files(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for file in os.listdir(src_folder):
        if file.endswith(".jpg"):
            shutil.move(os.path.join(src_folder, file), os.path.join(dest_folder, file))
    print("All .jpg files moved successfully.")