def isCorrectRect():
    point1 = (-7, 9)  # Координаты первой точки
    point2 = (3, 6)   # Координаты второй точки

    # Проверяем условия корректности
    if point1[0] > point2[0] or point1[1] > point2[1]:
        print("False")  # Некорректный прямоугольник
    else:
        print("True")   # Корректный прямоугольник
   
