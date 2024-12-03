from maps import maps, maps15, positions, positions15, winning_positions, winning_positions15
from colorama import Fore, Style, init
import os
from copy import deepcopy
# from time import time


def select_map_size():
    while True:
        player_input = input("Select map size (small - big): ")
        if player_input == 'small':
            return 'small'
        elif player_input == 'big':
            return 'big'
        else:
            print("Incorrect input.")


def set_difficulty():
    while True:
        player_input = input("Choose game difficulty(easy - medium - hard): ")
        if player_input == 'hard':
            return 2
        elif player_input == 'medium':
            return 1
        elif player_input == 'easy':
            return 0
        else:
            print("Incorrect input.")


def fog_of_war(matrix, diff, position):
    shown_matrix = deepcopy(matrix)
    if diff in [1, 2]:
        not_to_be_touched = []
        if diff == 2:
            not_to_be_touched = [position, [position[0] - 1, position[1]], [position[0] + 1, position[1]],
                                 [position[0], position[1] - 1], [position[0], position[1] + 1]]
        elif diff == 1:
            not_to_be_touched = [position, [position[0] - 1, position[1]], [position[0] + 1, position[1]],
                                 [position[0], position[1] - 1], [position[0], position[1] + 1],
                                 [position[0] - 1, position[1] - 1], [position[0] - 1, position[1] + 1], [position[0] +
                                                                                                          1, position[
                                                                                                              1] - 1],
                                 [position[0] + 1, position[1] + 1], [position[0] - 2, position[1]], [position[0] + 2,
                                                                                                      position[1]],
                                 [position[0], position[1] - 2], [position[0], position[1] + 2]]

        for row in range(len(matrix)):
            for value in range(len(matrix)):
                if [row, value] in not_to_be_touched:
                    pass
                else:
                    shown_matrix[row][value] = 9
    return shown_matrix


def show_map(matrix,number_map):
    if map_size == 'small':
        print(f'This is map number {number_map + 1} out of {len(maps)} maps.')
    elif map_size == 'big':
        print(f'This is map number {number_map + 1} out of {len(maps15)} maps.')
    init()
    for row in matrix:
        for value in row:
            if value == 1:
                print(Fore.RED + "■", end="  ")
            elif value == 0:
                print(Fore.GREEN + "■", end="  ")
            elif value == 2:
                print(Fore.CYAN + "■", end="  ")
            elif value == 9:
                print(Fore.WHITE + "■", end="  ")
            else:
                print(Fore.BLUE + "■", end="  ")
        print(Style.RESET_ALL)


def player_movement(matrix):
    # print(time())
    player_input = input("AWSD: ")
    # print(time())
    os.system('cls')
    if player_input == 'a':
        if matrix[current_position[0]][current_position[1] - 1] == 1:
            pass
        elif current_position[1] == 0:
            pass
        else:
            matrix[current_position[0]][current_position[1]] = 0
            current_position[1] -= 1
            matrix[current_position[0]][current_position[1]] = 2
    elif player_input == 'w':
        if matrix[current_position[0] - 1][current_position[1]] == 1:
            pass
        elif current_position[0] == 0:
            pass
        else:
            matrix[current_position[0]][current_position[1]] = 0
            current_position[0] -= 1
            matrix[current_position[0]][current_position[1]] = 2
    elif player_input == 's':
        if current_position[0] == (len(matrix) - 1):
            pass
        elif matrix[current_position[0] + 1][current_position[1]] == 1:
            pass
        else:
            matrix[current_position[0]][current_position[1]] = 0
            current_position[0] += 1
            matrix[current_position[0]][current_position[1]] = 2
    elif player_input == 'd':
        if current_position[1] == (len(matrix) - 1):
            pass
        elif matrix[current_position[0]][current_position[1] + 1] == 1:
            pass
        else:
            matrix[current_position[0]][current_position[1]] = 0
            current_position[1] += 1
            matrix[current_position[0]][current_position[1]] = 2


def next_map():
    global map_number, map_size, current_map, current_position, current_winning_position
    if map_size == 'small':
        if map_number == 8:
            return 0
    elif map_size == 'big':
        if map_number == 4:
            return 0
    if map_size == 'small':
        current_map = maps[map_number]
        current_position = positions[map_number]
        current_winning_position = winning_positions[map_number]
    elif map_size == 'big':
        current_map = maps15[map_number]
        current_position = positions15[map_number]
        current_winning_position = winning_positions15[map_number]
    return current_map, current_position, current_winning_position


def discovery(obfuscated_map, open_map, position):
    tiles_to_open = [position, [position[0] - 1, position[1]], [position[0] + 1, position[1]],
                     [position[0], position[1] - 1], [position[0], position[1] + 1],
                     [position[0] - 1, position[1] - 1], [position[0] - 1, position[1] + 1], [position[0] +
                                                                                              1, position[
                                                                                                  1] - 1],
                     [position[0] + 1, position[1] + 1], [position[0] - 2, position[1]], [position[0] + 2,
                                                                                          position[1]],
                     [position[0], position[1] - 2], [position[0], position[1] + 2]]
    for row in range(len(open_map)):
        for value in range(len(open_map)):
            if [row, value] in tiles_to_open:
                if obfuscated_map[row][value] == 2:
                    pass
                elif open_map[row][value] == 2:
                    pass
                else:
                    obfuscated_map[row][value] = open_map[row][value]


difficulty = set_difficulty()
map_size = select_map_size()
map_number = 0
# Logika gry:
while True:
    global easy_map
    # sprawdzenie warunku wygrania gry
    if map_size == 'small':
        if map_number == 8:
            print("Congratulations! You have completed the game!")
            break
    elif map_size == 'big':
        if map_number == 4:
            print("Congratulations! You have completed the game!")
            break
    # zaciągnięcie danych o mapie
    current_map, current_position, current_winning_position = next_map()
    if difficulty == 0:
        easy_map = fog_of_war(deepcopy(current_map), 1, current_position)
    os.system('cls')
    # loop, który odpowiada za odpowiedni fog of war w zależności od poziomu trudności oraz ruch gracza
    while True:
        if current_position == current_winning_position:
            break
        if difficulty == 0:
            show_map(easy_map, map_number)
            player_movement(easy_map)
            discovery(easy_map, current_map, current_position)
        else:
            show_map(fog_of_war(current_map, difficulty, current_position), map_number)
            player_movement(current_map)
    # zwiększenie numerka mapy po wygraniu
    map_number += 1
