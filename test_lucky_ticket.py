#!/usr/bin/env python

import unittest
import lucky_ticket


# Тестирование функции, оценивающей равенство половин числа
class PartsOfNumberTests(unittest.TestCase):

    # Этот тест должен привести к равенству
    def test_addition_equal(self):
        t_array = [0, 2, 9, 4, 3, 4]

        result = lucky_ticket.addition(t_array)

        self.assertEqual(result, True)

    # А этот тест - к неравенству
    def test_addition_not_equal(self):
        t_array = [6, 1, 0, 5, 8, 1]

        result = lucky_ticket.addition(t_array)

        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
