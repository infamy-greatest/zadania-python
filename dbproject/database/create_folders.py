import os


def create_folder(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Folder '{path}' has been created.")
        else:
            print(f"Folder '{path}' already exists.")
    except OSError as error:
        print(f"Error creating folder '{path}': {error}")


def create_all_folders():
    current_directory_path = os.getcwd()
    for first_folder in range(0, 10):
        folder_path = f'{current_directory_path}//{first_folder}'
        create_folder(folder_path)
        for second_folder in range(0, 10):
            folder_path = f'{current_directory_path}//{first_folder}//{second_folder}'
            create_folder(folder_path)
            for third_folder in range(0, 10):
                folder_path = f'{current_directory_path}//{first_folder}//{second_folder}//{third_folder}'
                create_folder(folder_path)
                for fourth_folder in range(0, 10):
                    folder_path = f'{current_directory_path}//{first_folder}//{second_folder}//{third_folder}//{fourth_folder}'
                    create_folder(folder_path)


if __name__ == '__main__':
    create_all_folders()
