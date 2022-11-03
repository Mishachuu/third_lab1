import os
import get_way
import shutil
import csv
import random


def copy_random_number(subdir):
    with open("random_annotation.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";")
        file_writer.writerow(["Абсолютный путь", "Относительный путь", "Класс"])
        for i in range(1020):
            rand_number = random.randint(0, 10000)
            if (os.path.isfile(get_way.get_absolute_way(subdir, i, "download")) == True):
                while(os.path.isfile(get_way.get_absolute_way(subdir, rand_number, "random")) == True):
                    rand_number = random.randint(0, 10000)
                shutil.copyfile(get_way.get_absolute_way(subdir, i, "download"), get_way.get_absolute_way(subdir, rand_number, "random"))
                file_writer.writerow([get_way.get_absolute_way(subdir, i, "download"), get_way.relative_way_random(rand_number), subdir])


def main():
        print("Начало")
        if not os.path.isdir("dataset/random_dataset"):
            os.makedirs("dataset/random_dataset")
        class_name = "cat"
        copy_random_number(class_name)
        class_name = "dog"
        copy_random_number(class_name)
        print("Конец")
    
    
if __name__ == "__main__":
        main()