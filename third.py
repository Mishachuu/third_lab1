import os
import get_way
import shutil
import csv
import random


def copy_random_number(subdir:str,folderpath) -> None:
    """скопирует данные(картинки) из директории dataset/subdir, а так же создаст csv файл

    Args:
        subdir (str): переменная, обозначающая подкаталог(класс)
    """
    with open("random_annotation.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\n")
        for i in range(1020):
            rand_number = random.randint(0, 10000)
            if (os.path.isfile(get_way.get_absolute_way(subdir, i, "download",folderpath)) == True):
                while (os.path.isfile(get_way.get_absolute_way(subdir, rand_number, "random",folderpath)) == True):
                    rand_number = random.randint(0, 10000)
                shutil.copyfile(get_way.get_absolute_way(
                    subdir, i, "download",folderpath), get_way.get_absolute_way(subdir, rand_number, "random"))
                file_writer.writerow([get_way.get_absolute_way(
                    subdir, i, "download",folderpath), get_way.relative_way_random(rand_number,folderpath), subdir])


def main(folderpath):
    print("Начало")
    if not os.path.isdir(f"{folderpath}/random_dataset"):
        os.makedirs(f"{folderpath}/random_dataset")
    with open("random_annotation.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\n")
        file_writer.writerow(
            ["Абсолютный путь", "Относительный путь", "Класс"])
    class_name = "cat"
    copy_random_number(class_name,folderpath)
    class_name = "dog"
    copy_random_number(class_name,folderpath)



if __name__ == "__main__":
    main()