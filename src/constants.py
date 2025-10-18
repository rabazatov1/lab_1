def get_tokens(s: str) -> list[str]:
    """Принимает на вход операции и отделяет их пробелами с двух сторон.

    Parameters
    ----------
    s : str

    Returns
    -------
    list[str]
        Стек с разделенными пробелами операциями
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


def binary_operations(symbol: str, num1: int | float, num2: int | float) -> int | float:
    """Выполняет все бинарные операции (если их возможно выполнить)

    Parameters
    ----------
    symbol : str
    num1 : int | float
    num2 : int | float

    Returns
    -------
    int | float
        Результат бинарной операции
    """
    match symbol:
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


def unary_operations(symbol: str, num: int | float) -> int | float:
    """Выполняет унарные операции

    Parameters
    ----------
    symbol : str
    num : int | float

    Returns
    -------
    int | float
        Результат унарной операции
    """
    match symbol:
        case '~':
            num *= -1
        case '$':
            num = num
    return num
