from random import random
import pickle
from multiprocessing import Process
import os


def populate_data(x, y):
    z = '0' * (9 - len(str(x))) + str(x)
    temporary_dict = {}
    for number in range(x, y):
        final_name = '0' * (9 - len(str(number))) + str(number)
        random_price = round(random() * 1.2 + 0.3, 2)
        temporary_dict[final_name] = random_price
    directory_path = f"{os.getcwd()}//{z[0]}//{z[1]}//{z[2]}//{z[3]}"
    z = f"{z}.pickle"
    full_file_path = os.path.join(directory_path, z)
    with open(full_file_path, "wb") as file:
        pickle.dump(temporary_dict, file)


def populate_folders_with_data():

    increment = 10000
    starting_number = 0

    current_task_number = 0

    for x in range(10000):
        with open("progress.txt", "r") as file:
            lines = file.readlines()
            first_line = int(lines[0].strip())
            second_line = int(lines[1].strip())

        z = '0' * (9 - len(str(starting_number))) + str(starting_number)
        full_file_path = f"{os.getcwd()}//{z[0]}//{z[1]}//{z[2]}//{z[3]}//{z[0:5]}0000.pickle"

        if os.path.isfile(full_file_path):
            print(f"Hash maps batch number {x + 1} out of 10000 has already been created before.")
            starting_number += (increment * 10)
            with open("progress.txt", "r") as file:
                lines = file.readlines()
                lines[0] = f"{x + 1}\n"
            with open("progress.txt", "w") as file:
                file.writelines(lines)
        else:
            thread_1 = Process(target=populate_data,
                               args=(starting_number, starting_number + increment))
            starting_number += increment

            thread_2 = Process(target=populate_data,
                               args=(starting_number, starting_number + increment))
            starting_number += increment

            thread_3 = Process(target=populate_data,
                               args=(starting_number, starting_number + increment))
            starting_number += increment

            thread_4 = Process(target=populate_data,
                               args=(starting_number, starting_number + increment))
            starting_number += increment

            thread_5 = Process(target=populate_data,
                               args=(starting_number, starting_number + increment))
            starting_number += increment

            thread_6 = Process(target=populate_data,
                               args=(starting_number, starting_number + increment))
            starting_number += increment

            thread_7 = Process(target=populate_data,
                               args=(starting_number, starting_number + increment))
            starting_number += increment

            thread_8 = Process(target=populate_data,
                               args=(starting_number, starting_number + increment))
            starting_number += increment

            thread_9 = Process(target=populate_data,
                               args=(starting_number, starting_number + increment))
            starting_number += increment

            thread_10 = Process(target=populate_data,
                                args=(starting_number, starting_number + increment))
            starting_number += increment

            thread_1.start()
            thread_2.start()
            thread_3.start()
            thread_4.start()
            thread_5.start()
            thread_6.start()
            thread_7.start()
            thread_8.start()
            thread_9.start()
            thread_10.start()

            thread_1.join()
            thread_2.join()
            thread_3.join()
            thread_4.join()
            thread_5.join()
            thread_6.join()
            thread_7.join()
            thread_8.join()
            thread_9.join()
            thread_10.join()
            current_task_number += 1
            print(f"Hash maps batch number {x + 1} out of 10000 has been created.")
            starting_number += (increment * 10)
            with open("progress.txt", "r") as file:
                lines = file.readlines()
                lines[0] = f"{x + 1}\n"
                lines[1] = f"{current_task_number}\n"
            with open("progress.txt", "w") as file:
                file.writelines(lines)


if __name__ == '__main__':
    # populate_data(999990000, 999990000 + 10000)
    # populate_data(0, 10000)
    populate_folders_with_data()
