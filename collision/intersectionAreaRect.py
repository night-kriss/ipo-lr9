class RectCorrectError():
    pass  # Исключение для ошибок с размерами

def intersectionAreaRect():
    rect1 = [(-7, 0), (13, 12)]  # Первый прямоугольник
    rect2 = [(-3, 1), (9, 10)]  # Второй прямоугольник

    # Координаты вершин
    x1, y1 = rect1[0]
    x2, y2 = rect1[1]
    x3, y3 = rect2[0]
    x4, y4 = rect2[1]

    # Границы пересечения
    left = max(x1, x3)   # Левая граница
    bottom = max(y1, y3) # Нижняя граница
    right = min(x2, x4)  # Правая граница
    top = min(y2, y4)    # Верхняя граница

    # Вычисляем ширину и высоту области пересечения
    width = right - left
    height = top - bottom

    if width < -10 or height < -10:
        raise RectCorrectError("Некорректные размеры прямоугольника")

    elif width <= 0 or height <= 0:
        print(0)  # Если нет пересечения

    else:
        print(width * height)  # Площадь пересечения
