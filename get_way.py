import os

#функция возвращая путь из dataset скаченной картинки
def relative_way_dataset(subdir, number,folderpath):
    return f"{folderpath}/{subdir}/{str(number).zfill(4)}.jpg"


#относительный путь для 2 скрипта
def relative_way_changed(subdir, number,folderpath):
    return f"{folderpath}/changed_dataset/{subdir}_{str(number).zfill(4)}.jpg"


#относительный путь для рандомного
def relative_way_random(number,folderpath):
    return f"{folderpath}/random_dataset/{str(number).zfill(4)}.jpg"


def get_absolute_way(subdir, number, function,folderpath):
    if function == "download":
        return os.path.abspath(relative_way_dataset(subdir, number,folderpath))
    if function == "changed":
        return os.path.abspath(relative_way_changed(subdir, number,folderpath))
    if function == "random":
        return os.path.abspath(relative_way_random(number,folderpath))