# Python строгая динамическая типизация
# The Zen of Python
# Установка модулей pip install pydantic
# https://pypi.org/
# PEP-8 - стили кода, PEP-257 - стили комментариев
import builtins


a = 1 + 2
  # | |
  # |  -- Операнд
  #   --- Оператор
# Оператнды: % (mod) - останок от деления
#            //(div) - целочисленное деление
snake_case = 0
I_AM_CONST = 3,14

# Keywords: False, None, True, and, as, assert, async, class, del, return ...
# Python library:
# 1) ===built-in functions and exceptions(без import): 
# abs(), aiter(), all(), any(), anext(), ascii()
# bin(), bool(), breakpoint(), bytearray(), bytes()
# callable(), chr(), classmethod(), compile(), complex()
# delattr(), dict(), divmod()
# enumerate(), eval(), exec()
# filter(), float(), format(), frozenset()
# getattr(), globals()
# hasattr(), hash(), help(), hex()
# id(), input(), int(), isinstance(), issubclass(), iter()
# len(), list(), locals()
# map(), max(), memoryview(), min()
# next()
# object(), oct(), open(), ord()
# print(), property()
# range(), repr(), reversed(), round()
# set(), setattr(), slice(), sorted(), staticmethod(), str(), sum(), super()
# tuple(), type()
# vars()
# zip()
# import()



            # https://docs.python.org/3/library/functions.html
# 2) The Python Standard Library()(входит в стандартный пакет):

# =====================Кодировка================================================
# ascii - code:       z=122---1 bite
#                0     ---    127 
#           (0000 0000 --- 0111 1111)

# utf8 - code:        z=122---1 bite  + 1-3 bite --- итого до 4 байт!!!
#                0     ---    127     
#           (0000 0000 --- 0111 1111)   
# utf-8 - представление unicode
# unicode -  стандарт кодирования символов, 
# кодовые точки от U+0000 до U+007F при ascii наборе и больше если другие символы
# Русская буква а
# 0b10000110000 <- Кодовая точка Unicode через ord
# 0b0000b100 0b00110000 <- Кодовая точка Unicode удобный вид
# 0b11010000 0b10110000 <- Представление "а" рус. через bytes()
#   110xxxxx   10xxxxxx <- х это значащие биты
#   |||        ||
#   ---        --
#   это шаблон определения количества октетов(их 2)
# ==============================================================================
# ================форматирование строк==========================================
# 1) ===printf-style String Formatting or interpolation operator
'%d' % a
# спецификаторы: 
# d, i - Signed integer decimal.
# o or %0o - Signed octal value.
# x or X - Signed hexadecimal (lowercase/uppercase).
# e or E - Floating point exponential format (lowercase/uppercase).
# f or F - Floating point decimal format.
# c - Single character (accepts integer or single character string).
# r - String (converts any Python object using repr()).
# s - String (converts any Python object using str()).
# 2) ===str.format()
'{0}, {1}, {02d}'.format('a', 'b', 'c')
'{:>30}, {:*^30}, {}'.format('a', 'b', 'c')  # use '*' as a fill char
"int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42) #'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
"int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42) #'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'
'Correct answers: {:.2%}'.format(1/2) #'Correct answers: 50%'
'{name:>15}! На счете {money:.2f}'.format(name='Jon', money=100)
# 3)===f-строки
f'{"Jon":>15}! На счете {100:.2f}'
# \n \t --- управляющие последовательности или escape-последовательности
# ==============================================================================
# =MAX=================Приоритет операторов================================================MIN
# (...), a**b, +a, a * b, a + b, a << b, a & b, a ^ b, a | b, a == b, not a, a and b, a or b
# Ассоциативность слева на право a + b +c
# Ассоциативность справа на лево a**b
# Нет ассоциативности, особая логика для a < b < c == (a < b) and (b < c)
# ============================================================================================

# аргументы позиционные, именованные, обязательные и необязательные
def f(pos1, pos2, /, pos_or_kwd, *(or *args), kwd1, kwd2, **kwargs):
#   -----------     ----------                 ----------
#     |             |                          |
#     |        Positional or keyword           |
#     |                                         - Keyword only
#      -- Positional only
    pass
# ==================Namespace and scope=========================================
# A namespace is a system that has a unique name for each and every object in Python.
# builtins namespace > Global namespace > local namespace
# (a,b,c) in namespace1 isolated (a,b,c) in namespace2
# Scope refers to the coding region from which a particular Python object is accessible
# Scope is a dictionary

# list method: append, extend, pop, insert, index
# dict method: get, setdefault, update, popitem, pop
#===================Виртуальное окружение. Модуль venv==========================
# python -m venv virt

#===================ООП=========================================================
# Атрибуты класса, атрибуты экземпляра
# Публичные, защищенные, приватные атрибуты
# Полиморфизм например 1) строка+строка
#             2) одинаковые название методоов разных классов dog.info, cat.info
#==================Ассинхронность===============================================
# Цикл событий, (корутина async def say_after(delay, what):)