import pickle
import os


def change_price():
    while True:
        n = input("Enter the number whose price you want to change (stop to stop): ")
        if n == "stop":
            break
        if n.isnumeric() == False or len(n) != 9:
            print("Given phone number is invalid.")
        else:
            try:
                price = float(input("What is the new price?: "))
                with open(
                        f"{os.getcwd()}//{n[0]}//{n[1]}//{n[2]}//{n[3]}//{n[0:5]}0000.pickle", "rb") as file:
                    hash_table = pickle.load(file)
                hash_table[n] = price
                with open(
                        f"{os.getcwd()}//{n[0]}//{n[1]}//{n[2]}//{n[3]}//{n[0:5]}0000.pickle", 'wb') as file:
                    pickle.dump(hash_table, file)
                print(f"New value: {price} successfully given to key: {n}")
            except Exception:
                print("Invalid input.")


def print_batch(n):
    if n.isnumeric() == False or len(n) != 9:
        return "Given batch number is invalid."
    else:
        try:
            with open(
                    f"{os.getcwd()}//{n[0]}//{n[1]}//{n[2]}//{n[3]}//{n[0:5]}0000.pickle", "rb") as file:
                hash_table = pickle.load(file)
                print(hash_table)
        except Exception:
            return "Given batch number is invalid."


if __name__ == "__main__":
    # change_price()
    print_batch('000030000')
    pass
