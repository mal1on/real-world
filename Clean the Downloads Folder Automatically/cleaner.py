"""
Python script, which when executed, deletes all files and directories
contained in Downloads folder.
"""

import os
import shutil


PATH = r"E:\temp\Downloads"


def cleaner():
    """Cleans downloads folder"""

    if os.path.exists(PATH):
        for item in os.listdir(PATH):
            item_path = os.path.join(PATH, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                print(
                    f"{item_path} is not a file or directory - leaving it untouched.")
        print(f"All files and directories deleted from {PATH}.")
    else:
        print(f"{PATH} does not exist or is not a directory.")


if __name__ == "__main__":
    cleaner()
