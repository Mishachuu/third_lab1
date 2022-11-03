import csv
import os
import get_way


def create_annotation(subdir):
    with open("annotation.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";",lineterminator='\n')
        file_writer.writerow(["Абсолютный путь", "Относительный путь", "Класс"])
        for i in range(1020) :
            if (os.path.isfile(get_way.get_absolute_way(subdir, i, "download")) == True ):
                file_writer.writerow([get_way.get_absolute_way(subdir, i, "download"), get_way.relative_way_dataset(subdir, i), subdir])

        
    
def main():
        print("Начало")
        subdir = "cat"
        create_annotation(subdir)
        subdir = "dog"
        create_annotation(subdir)
        print("Конец")
    
    
if __name__ == "__main__":
        main()