import os
import shutil
import csv

# копирование в другую директорию


def copy_to_another(subdir: str, folderpath) -> None:
    """копирует файлы(картинки) в другую директорию и создает csv файл и записывает туда абсолютный и относительный путь
    Args:
        subdir (str): название подкотолога(класса)
    """
    with open("annotation_changed.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\n")
        for i in range(1020):
            relative_way = f'dataset/changed_dataset/{subdir}_{str(i).zfill(4)}.jpg'
            absolute_way = os.path.abspath(relative_way)
            absolute_way_dataset = os.path.abspath(
                f"{folderpath}/{subdir}/{str(i).zfill(4)}.jpg")
            if (os.path.isfile(absolute_way_dataset) == True):
                shutil.copyfile(
                    absolute_way_dataset, absolute_way)
                file_writer.writerow([absolute_way, relative_way, subdir])


def main(folderpath):
    print("Начало")
    if not os.path.isdir(f"{folderpath}/changed_dataset"):
        os.makedirs(f"{folderpath}/changed_dataset")
    with open("annotation_changed.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\n")
        file_writer.writerow(
            ["Абсолютный путь", "Относительный путь", "Класс"])
    class_name = "cat"
    copy_to_another(class_name, folderpath)
    class_name = "dog"
    copy_to_another(class_name, folderpath)
    print("Конец")


if __name__ == "__main__":
    main('dataset/')
