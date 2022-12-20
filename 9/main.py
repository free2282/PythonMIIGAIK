import os
import glob
from pdf2docx import parse
from pathlib import Path
from docx2pdf import convert
from PIL import Image


def remFile(fileName):
    os.remove(os.path.abspath(fileName))
    print(f"Файл: \"{fileName}\" успешно удален!")


options = ["Сменить рабочий каталог",
           "Преобразовать PDF в docx",
           "Преобразовать docx в PDF",
           "Произвести сжатие изображений",
           "Удалить группу файлов",
           "Выход"]

selectedOption = -1
while True:
    print(f"Текущий каталог: {os.getcwd()}\n\nВыберите действие:\n")
    for i, v in enumerate(options, 0):
        print(f"{i}. {v}")
    selectedOption = int(input("\nВаш выбор: "))
    if selectedOption == 0:
        os.chdir(input("Укажите корректный путь к рабочему каталогу: "))
    elif selectedOption == 1:
        print("Список файлов с расширением .pdf в данном каталоге: \n")

        pdfFiles = glob.glob("*.pdf")
        for i, fileName in enumerate(pdfFiles, 0):
            print(f"{i+1}: {fileName}")

        fileIndex = int(input(
            "Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0):"))
        if fileIndex == 0:
            for pdfFile in pdfFiles:
                docxFile = Path(pdfFile).with_suffix('.docx')
                parse(pdfFile, docxFile)
        else:
            pdfFile = pdfFiles[fileIndex-1]
            docxFile = Path(pdfFile).with_suffix('.docx')
            parse(pdfFile, docxFile)
    elif selectedOption == 2:
        print("Список файлов с расширением .docx в данном каталоге: \n")

        docxFiles = glob.glob("*.docx")
        for i, fileName in enumerate(docxFiles, 0):
            print(f"{i+1}: {fileName}")

        fileIndex = int(input(
            "Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0):"))
        if fileIndex == 0:
            convert(os.getcwd())
        else:
            docxFile = docxFiles[fileIndex-1]
            pdfFile = Path(docxFile).with_suffix('.pdf')
            convert(docxFile, pdfFile)
    elif selectedOption == 3:
        print("Список файлов с расширением ('.jpeg', '.gif', '.png', '.jpg') в данном каталоге: \n")

        types = ('*.jpeg', '*.gif', '*.png', '*.jpg')
        imageFiles = []
        for t in types:
            imageFiles.extend(glob.glob(t))
        for i, fileName in enumerate(imageFiles, 0):
            print(f"{i+1}: {fileName}")

        fileIndex = int(input(
            "Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0):"))

        compressionQuality = int(
            input("Введите параметры сжатия (от 0 до 100%): "))

        if fileIndex == 0:
            for imageFile in imageFiles:
                imageFile = os.path.abspath(imageFile)
                img = Image.open(imageFile)
                img.save(imageFile, quality=compressionQuality)
        else:
            imageFile = os.path.abspath(imageFiles[fileIndex-1])
            img = Image.open(imageFile)
            img.save(imageFile, quality=compressionQuality)
    elif selectedOption == 4:
        action = int(input("Выберите действие: \n\n1. Удалить все файлы, начинающиеся на определенную подстроку\n2. Удилить все файлы, заканчивающиеся на определенную подстроку\n3. Удалить все файлы, содержащие определенную подстроку\n4. Удалить все файлы по расширению\nВведите номер действия: "))
        substring = input("Введите подстроку: ")
        print("\n")
        if action == 1:
            for fileName in os.listdir():
                if fileName.startswith(substring):
                    remFile(fileName)
        elif action == 2:
            for fileName in os.listdir():
                if os.path.splitext(fileName)[0].endswith(substring):
                    remFile(fileName)
        elif action == 3:
            for fileName in os.listdir():
                if substring in os.path.splitext(fileName)[0]:
                    remFile(fileName)
        elif action == 4:
            for fileName in os.listdir():
                if os.path.splitext(fileName)[1] == f".{substring}":
                    remFile(fileName)
    elif selectedOption == 5:
        exit()
    else:
        print("Неизвестная команда")
        exit()
