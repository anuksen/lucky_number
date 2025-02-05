#!/usr/bin/env python

import unittest
from lucky_ticket import is_lucky_ticket  # Импортируем функцию из вашего скрипта

class TestLuckyTicket(unittest.TestCase):
    def test_valid_lucky_ticket(self):
        # Тестируем корректные счастливые билеты
        self.assertTrue(is_lucky_ticket("123321"))  # 1+2+3 == 3+2+1
        self.assertTrue(is_lucky_ticket("000000"))  # 0+0+0 == 0+0+0
        self.assertFalse(is_lucky_ticket("111222"))  # 1+1+1 != 2+2+2 (несчастливый билет)

    def test_valid_non_lucky_ticket(self):
        # Тестируем корректные, но несчастливые билеты
        self.assertFalse(is_lucky_ticket("123456"))  # 1+2+3 != 4+5+6
        self.assertFalse(is_lucky_ticket("654321"))  # 6+5+4 != 3+2+1

    def test_invalid_ticket(self):
        # Тестируем некорректные данные
        self.assertFalse(is_lucky_ticket("12345"))   # Меньше 6 цифр
        self.assertFalse(is_lucky_ticket("1234567")) # Больше 6 цифр
        self.assertFalse(is_lucky_ticket("abcdef"))  # Не цифры
        self.assertFalse(is_lucky_ticket("123 45"))  # Пробелы
        self.assertFalse(is_lucky_ticket(""))        # Пустая строка

if __name__ == "__main__":
    unittest.main()
