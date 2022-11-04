import os
import get_way
import shutil
import csv

#копирование в другую директорию
def copy_to_another(subdir:str)->None:
    """копирует файлы(картинки) в другую директорию и создает csv файл и записывает туда абсолютный и относительный путь
    Args:
        subdir (str): название подкотолога(класса)
    """
    with open("annotation_changed.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\n")
        for i in range(1020):
            if (os.path.isfile(get_way.get_absolute_way(subdir, i, "download")) == True):
                shutil.copyfile(get_way.get_absolute_way(
                    subdir, i, "download"), get_way.get_absolute_way(subdir, i, "changed"))
                file_writer.writerow([get_way.get_absolute_way(
                    subdir, i, "download"), get_way.relative_way_changed(subdir, i), subdir])


def main(folderpath):
    print("Начало")
    if not os.path.isdir(f"{folderpath}/changed_dataset"):
        os.makedirs(f"{folderpath}/changed_dataset")
    with open("annotation_changed.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\n")
        file_writer.writerow(
            ["Абсолютный путь", "Относительный путь", "Класс"])
    class_name = "cat"
    copy_to_another(class_name)
    class_name = "dog"
    copy_to_another(class_name)
    print("Конец")


if __name__ == "__main__":
    main()