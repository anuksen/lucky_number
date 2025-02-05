#!/usr/bin/env python

def is_lucky_ticket(ticket_number):
    # Проверяем, что номер состоит из 6 цифр
    if len(ticket_number) != 6 or not ticket_number.isdigit():
        return False
    
    # Преобразуем строку в список целых чисел
    digits = [int(d) for d in ticket_number]
    
    # Сравниваем суммы первых трёх и последних трёх цифр
    return sum(digits[:3]) == sum(digits[3:])

def main():
    while True:
        # Запрашиваем номер билета у пользователя
        ticket_number = input("Напиши номер своего билета (6 цифр): ")
        
        # Проверяем, является ли билет счастливым
        if is_lucky_ticket(ticket_number):
            print("Да ты счастливчик!")
        else:
            print("Повезёт в следующий раз.")
        
        # Спрашиваем, хочет ли пользователь проверить ещё один билет
        again = input("Ещё билетик? y/n: ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
