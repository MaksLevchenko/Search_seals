from PIL import Image, ImageEnhance


# def split_image(image_path: str, piece: int = 2) -> bool:
#     """Разбиваем изображение на части"""
#     # Загрузка изображения
#     img = Image.open(image_path)

#     width, height = img.size

#     parts = []
#     if piece == 2:
#         parts.append(img.crop((0, 0, width // piece, height)))
#         parts.append(img.crop((width // piece, 0, width, height)))
#     if piece == 3:
#         for i in range(3):
#             left = (width // 3) * i
#             right = min((width // 3) * (i + 1), width)

#             part = img.crop((left, 0, right, height))
#             parts.append(part)

#     if piece == 4:
#         part_width = width // 2
#         part_height = height // 2

#         for i in range(2):
#             for j in range(2):
#                 left = j * part_width
#                 upper = i * part_height
#                 right = (j + 1) * part_width
#                 lower = (i + 1) * part_height

#                 part = img.crop((left, upper, right, lower))
#                 parts.append(part)
#     for idx, part in enumerate(parts):
#         part.save(f"search\\new_photo_{piece}\\part_{idx+1}.jpg", "JPEG")

#     return True


def resize_image(image_path: str, scale: float = 0.55) -> bool:
    """Уменьшает исходное фото и сохраняет его в отдельной папке"""
    img = Image.open(image_path)
    width, height = img.size
    new_width = int(width * scale)
    new_height = int(height * scale)

    resized_image = img.resize((new_width, new_height))
    name_image = image_path.split("\\")[-1]

    resized_image.save(
        f"search\\new_photo_resize\\{name_image}",
    )
    return True


def contrast_img(img):
    """Немного подкручивает контраст на фото"""
    enh = ImageEnhance.Contrast(image=img)
    return enh.enhance(1.8)
