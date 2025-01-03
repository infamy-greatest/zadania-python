import pickle
from time import time
import os

from dist_measuring_funcs import *
from phone_codes import phone_codes_dict
from country_coords import country_coords_dict


def phone_codes_to_distance(your_area_code, target_area_code):

    if your_area_code == target_area_code:
        return 0

    country_a = phone_codes_dict.get(your_area_code)
    country_b = phone_codes_dict.get(target_area_code)

    coords_a = country_coords_dict.get(country_a)
    coords_b = country_coords_dict.get(country_b)

    if coords_a is None and coords_b is not None:
        return "your country's phone area code is invalid."
    elif coords_b is None and coords_a is not None:
        return "target country's phone area code is invalid."
    elif coords_a is None and coords_b is None:
        return "both of the phone area codes are invalid."
    else:
        distance = getDistanceBetweenPointsNew(coords_a[0], coords_a[1], coords_b[0], coords_b[1])
        return distance


def distance_to_cost_multiplier(distance):
    if type(distance) == str:
        return distance
    else:
        multiplier = distance / 333
        multiplier = round(multiplier * 0.38, 3)
        return multiplier


def base_cost_determination(n):
    if n.isnumeric() is False or len(n) != 9:
        return "Given phone number is invalid (has to be exactly 9 numbers long and numeric)."
    else:
        with open(f"{os.getcwd()}//..//database//{n[0]}//{n[1]}//{n[2]}//{n[3]}//{n[0:5]}0000.pickle", "rb") as file:
            hash_table = pickle.load(file)
        phone_number_cost = hash_table.get(n)
        return phone_number_cost


def main():
    phone_number = input("Enter the phone number you are calling to: ")
    try:
        your_area_code = int(input("Enter your country's phone area code: "))
        target_area_code = int(input("Enter phone area code of the country you are calling to: "))
    except Exception:
        print("Given area codes are invalid.")
    start_time = time()
    distance = phone_codes_to_distance(your_area_code, target_area_code)
    multiplier = distance_to_cost_multiplier(distance)

    if multiplier is str:
        print(multiplier)
    else:
        base_cost = base_cost_determination(phone_number)
        final_cost = round((base_cost * multiplier), 2)
        end_time = time()
        print(f"The final cost of calling per minute is: {final_cost}\nThis calculation took: {round((end_time - start_time), 4)} seconds.")


if __name__ == '__main__':
    main()
