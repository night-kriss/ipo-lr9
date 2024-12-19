class RectCorrectError(Exception):
    pass # Исключение для ошибок с множеством прямоугольников

def intersectionAreaMultiRect(rectangles):
    if not rectangles:
        return 0  # Если список пустой, пересечение = 0
      
    for rect in rectangles:
        (x1, y1), (x2, y2) = rect
        if x1 >= x2 or y1 >= y2:
            raise RectCorrectError(f"Некорректный прямоугольник: {rect}")

    intersection = rectangles[0]  # Начинаем с первого прямоугольника

    # Поочередно пересекаем с каждым прямоугольником из списка
    for rect in rectangles[1:]:
        (x1, y1), (x2, y2) = intersection
        (x3, y3), (x4, y4) = rect

        # Границы пересечения
        left = max(x1, x3)
        bottom = max(y1, y3)
        right = min(x2, x4)
        top = min(y2, y4)

        if left < right and bottom < top:
            # Если есть пересечение, обновляем границы
            intersection = [(left, bottom), (right, top)]
        else:
            return 0  # Если пересечения нет, возвращаем 0

    # Вычисляем площадь
    (x1, y1), (x2, y2) = intersection
    return (x2 - x1) * (y2 - y1)


# Пример использования
rectangles_list = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)],
]

result = intersectionAreaMultiRect(rectangles_list)
print(f"Уникальная площадь пересечения: {result}")
