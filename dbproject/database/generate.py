from create_folders import *
from populate_data import *
import psutil
from time import sleep


def memory_check():
    print('\n')
    hdd = psutil.disk_usage('/')
    print(f'disk usage: {round(hdd.free / (2 ** 30), 2)}gb free out of '
          f'{round(hdd.total / (2 ** 30), 2)}gb total disk space.')
    if (round(hdd.free / (2 ** 30), 2)) < 21:
        print('You need more than 20,6gb of free disk space.')
    else:
        print('You have the required disk space (21gb~). ')
        print('\n')
        if input('Enter any key to proceed (stop to stop): ') == 'stop':
            return False
        else:
            return True


if __name__ == '__main__':
    if memory_check() == True:
        print("Creating all of the necessary folders in 3 seconds...")
        sleep(3)
        create_all_folders()
        print("\n" * 3)
        print("Folders created, populating them with data in 3 seconds...")
        print("\n" * 3)
        sleep(3)
        populate_folders_with_data()
        print("\n" * 3)
        print("All of the data has been created.")
    else:
        print('Creating database aborted.')
