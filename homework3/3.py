rom datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

def get_birth_date():
    while True:
        date_str = input("Введите дату рождения в формате день/месяц/год (например, 12/03/1995): ")
        parts = date_str.split("/")
        
        if len(parts) == 3 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
            if 1 <= day <= 31 and 1 <= month <= 12 and year <= datetime.now().year:
                return datetime(year, month, day)
        
        print("Неправильный формат даты. Попробуйте снова.")

def main():
    birth_date = get_birth_date()
    age = calculate_age(birth_date)
    print(f"Ваш возраст: {age} лет")

if __name__ == "__main__":
    main()
