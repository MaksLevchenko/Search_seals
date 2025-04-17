import os

from image_preparing import split_image
from process_image import process_image
from seals_print import seals_print


def main():

    # Проверяем, если файл result.txt существует, то удаляем его, чтобы протом записать новый
    if os.path.exists("result.txt"):
        os.remove("result.txt")

    # Проходим циклом по всем фото
    for image_path in os.listdir("search\\photo"):
        # Разбиваем фото на 2 части
        split_image(image_path=f"search\\photo\\{image_path}")
        # Разбиваем фото на 3 части
        split_image(image_path=f"search\\photo\\{image_path}", piece=3)
        # Разбиваем фото на 4 части
        split_image(image_path=f"search\\photo\\{image_path}", piece=4)

        # Проходим циклом по всем фото разделённых на 2 части
        seals_count = 0
        for i in range(2):
            count = process_image(f"search\\new_photo_2\part_{i+1}.jpg")
            seals_count += count

        # Проходим циклом по всем фото разделённых на 3 части
        seals_count_3 = 0
        for i in range(3):
            count = process_image(f"search\\new_photo_3\part_{i+1}.jpg")
            seals_count_3 += count

        # Проходим циклом по всем фото разделённых на 4 части
        seals_count_4 = 0
        for i in range(4):
            count = process_image(f"search\\new_photo_4\part_{i+1}.jpg")
            seals_count_4 += count

        # Сравниваем полученные результаты и выбираем максимальный
        seals_count = max(seals_count, seals_count_3, seals_count_4)

        # Загоняем в нейросеть оригинальное фото
        count = process_image(image_path=f"search\\photo\\{image_path}")
        path = image_path.split("\\")[-1]

        # Сравниваем полученные результаты, выбираем максимальный и записываем результат в файл
        if seals_count > count:
            seals = seals_print(seals_count=seals_count)
            with open("result.txt", "a", encoding="utf-8") as file:
                file.write(f"На изображении: {path}, {seals_count} {seals}.\n")
        else:
            seals = seals_print(seals_count=count)
            with open("result.txt", "a", encoding="utf-8") as file:
                file.write(f"На изображении: {path}, {count} {seals}.\n")


if __name__ == "__main__":
    main()
