from src.errors import check_all_errors, is_number, FormatError


def get_tokens(s: str) -> list[str]:
    """
    Заменяет операторы на их версии с пробелом с обеих сторон

    :param s: Входная строка с выражением
    :type s: str
    :return: Список токенов с разделёнными операциями
    :rtype: list[str]
    """
    changes = {
        '+': ' + ',
        '-': ' - ',
        '//': ' :: ',
        '%': ' % ',
        '**': ' ^^ ',
        '~': ' ~ ',
        '$': ' $ ',
        '(': ' ( ',
        ')': ' ) '
    }
    for old, new in changes.items():
        s = s.replace(old, new)
    s = s.replace('*', ' * ')
    s = s.replace('/', ' / ')
    s = s.replace('^^', '**')
    s = s.replace('::', '//')
    return s.split()


def binary_operations(token: str, num1: float, num2: float) -> float:
    """
    Выполняет бинарные операции над двумя числами

    :param token: Оператор для выполнения
    :type token: str
    :param num1: Левый операнд
    :type num1: float
    :param num2: Правый операнд
    :type num2: float
    :raises ZeroDivisionError: Если выполняется деление на ноль
    :raises: ValueError: Если операции // или % выполняются с числами, у которых ненулевая дробная часть
    """
    match token:
        case '+':
            num1 += num2
        case '-':
            num1 -= num2
        case '*':
            num1 *= num2
        case '/':
            try:
                num1 /= num2
            except ZeroDivisionError:
                raise ZeroDivisionError("На ноль делить нельзя")
        case '//':
            if not num1.is_integer() or not num2.is_integer():
                raise ValueError("Необходимо, чтобы все операции «//» выполнялись с целыми числами")
            try:
                num1 //= num2
            except ZeroDivisionError:
                raise ZeroDivisionError("На ноль делить нельзя")
        case '%':
            if not num1.is_integer() or not num2.is_integer():
                raise ValueError("Необходимо, чтобы все операции «%» выполнялись с целыми числами")
            try:
                num1 %= num2
            except ZeroDivisionError:
                raise ZeroDivisionError("На ноль делить нельзя")
        case '**':
            num1 **= num2
    return num1


def unary_operations(token: str, num: float) -> float:
    """
    Выполняет унарные операции над числом

   :param token: Оператор для выполнения
   :type token: str
   :param num: Число, к которому применяется унарная операция
   :type num: float
   :return: Результат после выполнения унарной операции
   :rtype: float
    """
    match token:
        case '~':
            num *= -1
        case '$':
            num = num
    return num


def tech_part(s: str) -> float | None:
    """
    Обрабатывает выражение согласно обратной польской нотации: числа добавляются по одному в созданный стек, а
операции выполняются над элементами этого же стека

    :param s: Входная строка с выражением
    :type s: str
    :return: Результат всех вычислений в выражении (None использовано для соблюдения правил синтаксиса языка, сама
 же функция никогда не будет возвращать None)
    :rtype: float | None
    raises FormatError: Если количество операндов не соответствует количеству операций
    """
    tokens = get_tokens(s)
    if check_all_errors(tokens):
        stack = []
        for token in tokens:
            if is_number(token):
                stack.append(float(token))
            elif token in "+-%**//":
                if len(stack) >= 2:
                    stack.append(binary_operations(
                        token, stack.pop(-2), stack.pop(-1)))
                else:
                    raise FormatError("Количество операндов не соответствует количество операций")

            elif token in "~$":
                stack.append(unary_operations(token, stack.pop(-1)))

        return stack[-1]
    return None
