from converter import main
import unittest


class TestSum(unittest.TestCase):

    def test_empty_args(self):
        ''' Тестирование при отсутствии аргумента '''
        self.assertEqual(main(['converter.py']), 1)

    def test_many_args(self):
        ''' Тестирование при множественном вводе аргументов '''
        self.assertEqual(main(['converter.py', '213', '12332']), 2)

    def test_incorrect_args(self):
        ''' Тестирование при некорректном (не числовом) аргументе '''
        self.assertEqual(main(['converter.py', '2w13']), 3)

    def test_negative_args(self):
        ''' Тестирование при отрицательном аргументе '''
        self.assertEqual(main(['converter.py', '-123']), 4)

    def test_small_number_args(self):
        ''' Тестирование при малом значении аргумента '''
        self.assertEqual(main(['converter.py', '0.001']), 0)

    def test_huge_number_args(self):
        ''' Тестирование при большом значении аргументе '''
        self.assertEqual(main(['converter.py', '5532535232366632622636233265544554']), 0)

    def test_correct_args(self):
        self.assertEqual(main(['converter.py', '2000',]), 0)


if __name__ == '__main__':
    unittest.main()
