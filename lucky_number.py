# Объявляем пустой массив ticket для цифр целочисленного типа
ticket = []
again = 'y'
# Зацикливаем программу, пока пользователь не введёт любое значение
while again == 'y':

    if again == 'y':

        # Получаем номер от пользователя и готовим его к дальнейшей работе
        while len(ticket) < 6:
            # Вводим номер билета
            ticket_str = input("Напиши номер своего билета(6 цифр): ")

            for i in range(6):
                # Отбраковка длинных номеров
                if len(ticket_str) > 6:
                    print("Цифр не должно быть больше шести")
                    break
                try:
                    # Добавляем проверенную цифру в массив
                    ticket.append(int(ticket_str[i]))
                # Отбраковка посторонних символов
                except ValueError:
                    print(f"Введённый символ '{ticket_str[i]}' - не цифра.")
                    ticket = []
                    break
                # Отбраковка коротких номеров
                except IndexError:
                    print("Недостаточно цифр")
                    ticket = []
                    break

        # Суммируем первые три и последние три цифры билета
        part1 = ticket[0]+ticket[1]+ticket[2]
        part2 = ticket[3]+ticket[4]+ticket[5]
        # Сравниваем суммы и выносим вердикт
        if part1 == part2:
            print("Да ты счастливчик!")
        else:
            print("Повезёт в следующий раз.")
        ticket = []
        again = input("Ещё билетик? y/n: ")
    else:
        break
