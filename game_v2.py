"""Игра угадывает число """

import numpy as np
def random_predict(number:int=1) -> int:
    count = 0
    while True:
        count +=1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла если угадали
    return(count)
# print(f'количество попыток  : {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыткок в среднем за 1000 проходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls =[] # список для сохранения количества попыток
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = (1000)) #загадываем 1000 случайных чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) # находим среднее число попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ =='__main__':
    #RUN
    score_game(random_predict)