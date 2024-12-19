class RectCorrectError(Exception):
   pass # Исключение для некорректных прямоугольников

def isCollisionRect():
    rect1 = [(-3.4, 1), (9.2, 10)]    # Первый прямоугольник
    rect2 = [(-7.4, 0), (13.2, 12)]  # Второй прямоугольник

    # Координаты прямоугольников
    x1_rect1, y1_rect1 = rect1[0]
    x2_rect1, y2_rect1 = rect1[1]
    x1_rect2, y1_rect2 = rect2[0]
    x2_rect2, y2_rect2 = rect2[1]    

    # Проверка пересечения по оси Y
    if y2_rect1 < y1_rect2 or y2_rect2 < y1_rect1:
        raise RectCorrectError("Некорректный прямоугольник")  # Ошибка

    # Проверка пересечения по оси X
    elif x2_rect1 < x1_rect2 or x2_rect2 < x1_rect1:
        print("False")  # Нет пересечения

    else:
        print("True")   # Есть пересечение

