from src.constants import get_tokens, binary_operations,unary_operations
from src.errors import check_all_errors, is_number, FormatError


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
