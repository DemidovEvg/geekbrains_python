import unittest
# run: py -m unittest -v work\unittest_.py
# run: py -m unittest -v work.unittest_
# run: py -m unittest -v work.unittest_.TestClass
# run: py -m unittest -v work.unittest_.TestClass.test_init0
# py -m unittest discover -s work -p "unittest*.py"
# unittest -v - детальный отчет
# unittest -b - вывод программы при провале будет показан
# unittest -c - ctrl+C во время теста ожидает завершения теста и затем сообщает результаты
# unittest -f - выход после первого же неудачного теста
# unittest --locals - показывает локальные переменные для провалившихся тестов
# or unittest.main()
# test fixture, test case, test suite, test runner

# Класс которые тестируем
class Equation:
    def __init__(self, a=0, b=0, c=0):
        if a == 0 and b == 0:
            raise ValueError("a and b can't equal zerro at the same time")
        self.a = a
        self.b = b
        self.c = c

    def f(self, x):
        return self.a*x**2 + self.b*x + self.c

    def type_equation(self):
        if self.a != 0:
            return 'parabola'
        else:
            return 'line'
        
    def is_open_to_the_top(self):
        return True if self.a > 0 else False

    def vertex(self):
        x0 = - self.b/2*self.a
        y0 = self.a*x0**2 + self.b*x0 + self.c
        return (x0, y0)
    
    def __str__(self):
        def format_num(num, first_place = False):
            if num == 0:
                return ''
            if num == 1:
                return '' if first_place else '+'
            if num == -1:
                return '-'
            if num > 0:
                return f'{num:}' if first_place else f'{num:+}'
            if num < 0:
                return f'{num:-}'         
        equation = ''
        cur_first_place=True
        if self.a != 0:
            equation += f'{format_num(self.a, first_place=cur_first_place)}x\u00b2'
            cur_first_place = False
        if self.b != 0:
            equation += f'{format_num(self.b, first_place=cur_first_place)}x'
            cur_first_place = False
        if self.c != 0:
            equation += f'{format_num(self.c, first_place=cur_first_place)}'
        return equation

# ==============================================
# Класс которым тестируем
class TestClass(unittest.TestCase):
    import sys
    @classmethod
    def setUpClass(cls):
        cls.parabola = Equation(1,2,3)

    @classmethod
    def tearDownClass(cls):
        del cls.parabola

    def setUp(self):
        'Инициализация перед тестом'
    
    def tearDown(self):
        'Я подчищаю после теста'

    def test_init0(self):
        self.assertEqual(str(Equation(1,2,3)), 'x²+2x+3')

    def test_init1(self):
        self.assertEqual(str(Equation(-3,3,0)), '-3x²+3x')

    # def test_TypeError(self):
    #     with self.assertRaises(ValueError):
    #         Equation(0,0,10)

    @unittest.skip("пропускаем тест")
    def test_nothing(self):
        self.fail("немедленное ошибка")

    @unittest.skipIf(sys.version_info.major == 3 and sys.version_info.minor == 10, 
                     'Версия python не равна 3.10')
    def test_nothing2(self):
        self.fail("немедленное ошибка")

    # @unittest.skipUnless(sys.platform.startswith("win"),
    #                      'Пропускаем несли не windows')
    # def test_nothing3(self):
    #     self.fail("немедленное ошибка")

    # @unittest.expectedFailure
    # def test_nothing3(self):
    #     self.fail("немедленное ошибка")

    def test_is_open_to_the_top(self):
        for n in range(1, 5):
            p1 = Equation(n)
            with self.subTest(i=n):
                self.assertTrue(p1.is_open_to_the_top())

if __name__ == '__main__':
    unittest.main()

    