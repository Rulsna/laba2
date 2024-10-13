import random

def play_round():
    choices = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(choices)
    
    user_choice = input("Выберите: камень, ножницы или бумага? ").lower().strip()  # удаляем лишние пробелы
    while user_choice not in choices:
        print("Неверный выбор. Попробуйте снова.")
        user_choice = input("Выберите: камень, ножницы или бумага? ").lower().strip()

    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        print("Вы победили!")
    else:
        print("Компьютер победил!")

def main():
    while True:
        play_round()
        again = input("Хотите сыграть ещё раз? (да/нет): ").lower().strip()
        if again != "да":
            break

if __name__ == "__main__":
    main()
