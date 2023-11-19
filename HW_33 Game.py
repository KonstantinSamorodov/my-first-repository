import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    start = 0
    end = 101
    count = 1
    while True:
        predict = (start + end) // 2
        if number == predict:
            break
        count += 1
        if number > predict:
            start = predict
        elif number < predict:
            end = predict


    # Ваш код заканчивается здесь

    return count
print(game_core_v3)

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)

