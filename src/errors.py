def is_number(symbol):
    try:
        float(symbol)
        return True
    except ValueError:
        return False


class FormatError(Exception):
    pass


class BracketsError(FormatError):
    pass


def right_symbols(loc_tokens):
    """Проверяет, все ли символы корректные

    Parameters
    ----------
    loc_tokens : list[str]

    Raises
    ------
    SyntaxError
    """
    for symbol in set(loc_tokens):
        if not is_number(symbol) and symbol not in '+-**//%$~()':
            raise SyntaxError(f"Символ {symbol} недопустим в программе")


def right_expression(loc_tokens):
    nums = 0
    opers = 0
    for symbol in loc_tokens:
        if is_number(symbol):
            nums += 1
        elif symbol in '+-**//%':
            opers += 1
    if nums != opers + 1:
        raise FormatError("Количество операндов не соответствует количество операций")


def brackets(loc_tokens):
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


def empty_line(loc_tokens):
    if len(loc_tokens) == 0:
        raise ValueError("Введена пустая строка")


def check_all_errors(loc_tokens):
    empty_line(loc_tokens)
    right_symbols(loc_tokens)
    brackets(loc_tokens)
    right_expression(loc_tokens)
    return True
