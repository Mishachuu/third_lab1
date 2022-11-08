import csv
import os

def create_annotation(subdir:str, folderpath) -> None:
    """создает csv файл и записывает туда абсолют. и относит. путь файла

    Args:
        subdir (str): название подкаталога(класса)
    """
    with open("annotation.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator='\n')
        for i in range(1020):
            relative_way = f'dataset/{subdir}/{str(i).zfill(4)}.jpg'
            absolute_way = f'{folderpath}/{subdir}/{str(i).zfill(4)}.jpg'
            if (os.path.isfile(absolute_way)) == True:
                file_writer.writerow([absolute_way, relative_way, subdir])


def main(folderpath):
    print("Начало")
    with open("annotation.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator='\n')
        file_writer.writerow(
            ["Абсолютный путь", "Относительный путь", "Класс"])
    subdir = "cat"
    create_annotation(subdir,folderpath)
    subdir = "dog"
    create_annotation(subdir,folderpath)
    print("Конец")


if __name__ == "__main__":
    main('dataset/')