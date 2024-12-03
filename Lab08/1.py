def factorial(n):
    if n == 1:
        return n
    else:
        return factorial(n - 1) * n

def main():
    print(factorial(12))

if __name__ == "__main__":
    main()