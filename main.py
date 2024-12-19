# Импортируем функции из модуля collision
from collision import isCorrectRect, isCollisionRect, intersectionAreaRect, intersectionAreaMultiRect

# Проверяем корректность прямоугольника с помощью функции isCorrectRect
isCorrectRect.isCorrectRect()

# Проверяем пересечение двух прямоугольников с помощью функции isCollisionRect
isCollisionRect.isCollisionRect()

# Вычисляем площадь пересечения двух прямоугольников с помощью функции intersectionAreaRect
intersectionAreaRect.intersectionAreaRect()

# Определяем список прямоугольников для вычисления общей площади пересечения
rectangles = [
    [(-3, 1), (9, 10)],  # Первый прямоугольник
    [(-7, 0), (13, 12)], # Второй прямоугольник
    [(0, 0), (5, 5)],    # Третий прямоугольник
    [(2, 2), (7, 7)]     # Четвертый прямоугольник
]
# Вычисляем уникальную площадь пересечения всех прямоугольников с помощью функции intersectionAreaMultiRect
intersectionAreaMultiRect.intersectionAreaMultiRect(rectangles)       
