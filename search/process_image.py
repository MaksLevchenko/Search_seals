from ultralytics import YOLO
import cv2
from PIL import Image

from image_preparing import contrast


# Загрузка модели YOLOv8
model = YOLO("seals_best.pt")


# Функция для обработки изображения
def process_image(image_path: str, contrast: bool = False) -> int:
    """Обрабатываем изображение с помощью нейросети"""

    # Загрузка изображения
    if contrast:
        image = contrast(Image.open(image_path))
    else:
        image = cv2.imread(image_path)
    results = model(image)[0]

    return len(results.boxes)
