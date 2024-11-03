import numpy as np

def guess_function(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное программой число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    # Предполагаемое число (отгадка для number). Выбирается из диапазона от 1 до 100
    predict = np.random.randint(1, 101)
    
    # Количество попыток
    count = 0
    # Задаем первоначальные минимальное и максимальное число
    predict_h = 100
    predict_l = 1
    while True:
        # Считаем количество попыток
        count+=1
        # Если предполагаемое число больше загаданного,
        # Предполагаемое число становится верхней границей и выбирается число посередине
        if predict > number:
            predict_h = predict
            predict = (predict_h + predict_l)//2
        # Если предполагаемое число меньше загаданного, 
        # Предполагаемое число становится нижней границей и выбирается число посередине
        elif predict < number:
            predict_l = predict
            predict = (predict_h + predict_l)//2
        # В других случаях число отгадано, цикл останавливается
        else:
            break
    return count

def guess_game(guess_function) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        guess_function (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    # Создали лист для подсчетов
    count_ls = []
    # Фиксируем сид для воспроизводимости
    np.random.seed(1) 
    # Загадали список чисел
    random_array = np.random.randint(1, 100, 1000)
    
    # Проходим циклом по загаданным числам в списке
    for number in random_array:
        # Добвляем результат в список
        count_ls.append(guess_function(number))
    
    # Считаем среднее количество попыток
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score


guess_game(guess_function)