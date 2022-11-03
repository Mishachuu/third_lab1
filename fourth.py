from Iterator import iterator


def main():
    print('Начало. Введите метку (cat/dog)')
    mark=input()
    val = iterator('annotation.csv', mark)
    for way in val:
        print(way)
    print('Конец')
    
    
if __name__ == "__main__":
    main()