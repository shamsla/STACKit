import os
import shutil
from files_extensions import *
from random import randrange


def checkFiles(path):  # CHECKS THAT IS FILES EXISTS OR NOT IN GIVEN FOLDER
    filesList = os.listdir(path)
    for f in filesList:
        if os.path.isfile(rf"{path}/{f}"):
            return True
    return False


def evaluate(fileType, path):  # CHECKS IF FILES WITH GIVEN EXT EXISTS THEN CREATE FOLDER

    filesList = os.listdir(path)
    for f in filesList:
        for ext in files[fileType]:
            if f.endswith(ext):
                return True
    return False


def otherFiles(path):  # CREATE FOLDER FOR OTHER FILES
    filesList = os.listdir(path)

    if not os.path.isdir(rf"{path}/Other Separated Files"):
        # if Other Separated Files folder not exists then create it
        os.mkdir(rf"{path}/Other Separated Files")

    for f in filesList:
        if os.path.isfile(rf"{path}/{f}"):
            if os.path.exists(rf"{path}/Other Separated Files/{f}") == False:
                # if the file not exists in the Other Separated Files folder already then move the file
                shutil.move(rf"{path}/{f}", rf"{path}/Other Separated Files")
            else:
                # AND if the file already exists then chage the name of that file
                shutil.move(
                    rf"{path}/{f}", rf"{path}/Other Separated Files/Another_{randrange(991,100000)}_{f}")

    if not os.listdir(rf"{path}/Other Separated Files"):
        # if no file moved to the Other Separated Files folder then remove this folder
        os.rmdir(rf"{path}/Other Separated Files")


# MAIN FUNCTION FOR CUSTOM SEPARATOR[Extension]
def csMain(path, mainPath, extension):
    """
    Main function for moving the files with custom extension(s)
    """

    # mainPath -> simply the extension name in uppercase

    # check separator() for var i
    i = 0  # INDICATES THAT FILES MOVED OR NOT

    if '.' not in extension:
        # if there is no dot with extension name
        extension = f".{extension}"

    filesList = os.listdir(path)
    if not os.path.isdir(rf"{path}/.{mainPath} FF"):
        os.mkdir(rf"{path}/.{mainPath} FF")

    for f in filesList:
        if os.path.isfile(rf"{path}/{f}"):
            if f.endswith(extension):
                # IF FILE ALREADY NOT EXISTS
                if os.path.exists(rf"{path}/.{mainPath} FF/{f}") == False:
                    shutil.move(rf"{path}/{f}", rf"{path}/.{mainPath} FF")
                    i += 1
                else:  # IF FILE ALREADY EXISTS
                    shutil.move(
                        rf"{path}/{f}", rf"{path}/.{mainPath} FF/Another_{randrange(991,100000)}_{f}")
                    i += 1

    # REMOVES THE CREATED FOLDER IF EMPTY
    if not os.listdir(rf"{path}/.{mainPath} FF"):
        os.rmdir(rf"{path}/.{mainPath} FF")

    if i > 0:
        # check separator for var i
        return True
    else:
        return False
