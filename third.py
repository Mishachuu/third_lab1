import os
import shutil
import csv
import random


def copy_random_number(subdir: str, folderpath) -> None:
    """скопирует данные(картинки) из директории dataset/subdir, а так же создаст csv файл

    Args:
        subdir (str): переменная, обозначающая подкаталог(класс)
    """
    with open("random_annotation.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\n")
        for i in range(1020):
            rand_number = random.randint(0, 10000)
            relative_way = f'dataset/random_dataset/{rand_number}.jpg'
            absolute_way = os.path.abspath(relative_way)
            absolute_way_dataset = os.path.abspath(
                f"{folderpath}/{subdir}/{str(i).zfill(4)}.jpg")
            if (os.path.isfile(absolute_way_dataset) == True):
                while (os.path.isfile(absolute_way) == True):
                    rand_number = random.randint(0, 10000)
                shutil.copyfile(
                    absolute_way_dataset, absolute_way)
                file_writer.writerow([absolute_way, relative_way, subdir])


def main(folderpath):
    print("Начало")
    if not os.path.isdir(f"{folderpath}/random_dataset"):
        os.makedirs(f"{folderpath}/random_dataset")
    with open("random_annotation.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\n")
        file_writer.writerow(
            ["Абсолютный путь", "Относительный путь", "Класс"])
    class_name = "cat"
    copy_random_number(class_name, folderpath)
    class_name = "dog"
    copy_random_number(class_name, folderpath)


if __name__ == "__main__":
    main('dataset/')
