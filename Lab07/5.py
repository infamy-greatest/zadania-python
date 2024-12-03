def merge_dicts(dict1, dict2):
    return dict1 | dict2


if __name__ == "__main__":
    dict01 = {1: 10, 2: 7, 3: 8, 4: 15, 5: 14, 6: 3, 7: 2}
    dict03 = {8: 10, 9: 40, 1: 55}
    merged_dict = merge_dicts(dict01, dict03)
    print(merged_dict)
