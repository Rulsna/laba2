import random

def find_multiples():
    while True:
        x = input("Введите число X, которому должны быть кратны числа: ")
        if x.isdigit() and int(x) != 0:
            x = int(x)
            break
        print("Введите корректное целое число больше нуля.")

    numbers = [random.randint(0, 200) for _ in range(10)]
    print("Сгенерированные числа:", numbers)

    multiples = list(filter(lambda n: n % x == 0, numbers))
    print(f"Числа, кратные {x}: {multiples}")

if __name__ == "__main__":
    find_multiples()
