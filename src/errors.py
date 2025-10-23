class FormatError(Exception):
    """Исключение для ошибок, связанных с форматом входного выражения(количеством операций и операндов)"""
    pass


class BracketsError(FormatError):
    """Исключение для ошибок, связанных со скобками в выражении"""
    pass


def is_number(token) -> bool:
    """
    Проверяет, можно ли преобразовать токен в число

    :param token: проверяемый токен
    :type token: str
    :return: True, если можно преобразовать токен в число, иначе False
    :rtype: bool
    """
    try:
        float(token)
        return True
    except ValueError:
        return False


def empty_line(loc_tokens):
    """
    Проверяет, что выражение не пустое

    :param loc_tokens: Список токенов
    :type loc_tokens: list[str]
    :raises ValueError: Если выражение пустое
    """
    if len(loc_tokens) == 0:
        raise ValueError("Введена пустая строка")


def right_tokens(loc_tokens):
    """
    Проверяет, все ли токены в выражении допустимы

    :param loc_tokens: Список токенов
    :type loc_tokens: list[str]
    :raises SyntaxError: Если найден хотя бы один недопустимый токен
    """
    for token in set(loc_tokens):
        if not is_number(token) and token not in '+-**//%$~()':
            raise SyntaxError("Найдем недопустимый токен (в программе могут использоваться только корректно записанные \
числа, операторы из '+-**//%$~' и скобки")


def brackets(loc_tokens):
    """
    Проверяет, верно ли расставлены скобки в выражении

    :param loc_tokens: Список токенов
    :type loc_tokens: list[str]
    :raises BracketsError: Если скобки расставлены неправильно
    """
    if loc_tokens.count("(") != loc_tokens.count(")"):
        raise BracketsError("Неправильно расставлены скобки (лучше уберите их)")
    while '(' in loc_tokens:
        loc_tokens.reverse()
        index = len(loc_tokens) - 1 - loc_tokens.index('(')
        loc_tokens.reverse()
        nums = 0
        opers = 0
        bin_opers = 0
        for i in range(index + 1, len(loc_tokens)):
            if loc_tokens[i] != ')':
                if is_number(loc_tokens[i]):
                    nums += 1
                elif loc_tokens[i] in '$~':
                    bin_opers += 1
                else:
                    opers += 1
            else:
                if nums != opers + 1 or bin_opers > 0 and nums == 0:
                    raise BracketsError("Неправильно расставлены скобки (лучше уберите их)")
                else:
                    del loc_tokens[index], loc_tokens[i - 1]
                    break


def right_expression(loc_tokens):
    """
    Проверяет, соответствует количество операндов количеству операций в выражении

    :param loc_tokens: Список токенов
    :type loc_tokens: list[str]
    :raises FormatError: Если количество операндов не соответствует количеству операций
    """
    nums = 0
    opers = 0
    for token in loc_tokens:
        if is_number(token):
            nums += 1
        elif token in '+-**//%':
            opers += 1
    if nums != opers + 1:
        raise FormatError("Количество операндов не соответствует количество операций")


def check_all_errors(loc_tokens) -> bool:
    """
    Проверяет выражение на все возможные ошибки

    :param loc_tokens: Список токенов
    :type loc_tokens: list[str]Й
    :return: True, если все проверки пройдены успешно
    :rtype: bool
    :raises ValueError: Если выражение пустое
    :raises SyntaxError: Если найден хотя бы один недопустимый символ
    :raises BracketsError: Если скобки расставлены неправильно
    :raises FormatError: Если количество операндов не соответствует количество операций
    """
    empty_line(loc_tokens)
    right_tokens(loc_tokens)
    brackets(loc_tokens)
    right_expression(loc_tokens)
    return True
