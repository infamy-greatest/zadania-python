def find_max(dictionary):
    key = max(dictionary, key=dictionary.get)
    value = dictionary[key]
    return value


if __name__ == "__main__":
    my_dict = {1: 10, 2: 7, 3: 8, 4: 15, 5: 14}
    max_value = find_max(my_dict)
    print(f"Maksymalna wartość: {max_value}")
