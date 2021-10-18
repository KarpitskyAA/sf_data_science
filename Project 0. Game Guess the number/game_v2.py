"""Игра угадывает число """

import numpy as np
def binary_predict(number:int=1) -> int:
    count = 0 # Счетчик числа попыток
    left_bound = 1 # изначальная левая граница интервала для отгадывания числа
    right_bound = 100 # изначальная правая граница интервала для отгадывания числа
    while True:
        count +=1
        predict_number = (left_bound + right_bound) // 2 # предполагаемое число
        if number == predict_number:
            break # выход из цикла если угадали
        elif number > predict_number:
            left_bound = predict_number # изменяем левую границу, если загаданное число больше нашего
        else:
            right_bound = predict_number # изменяем правую границу, если загаданное число меньше нашего
    return(count)

def score_game(binary_predict) -> int:
    """ За какое количество попыткок в среднем за 1000 проходов угадывает наш алгоритм

    Args:
        binary_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls =[] # список для сохранения количества попыток
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 100, size = (1000)) #загадываем 1000 случайных чисел
    for number in random_array:
        count_ls.append(binary_predict(number))
    score = int(np.mean(count_ls)) # находим среднее число попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    #RUN
    score_game(binary_predict)