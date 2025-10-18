from src.constants import get_tokens, binary_operations,unary_operations
from src.errors import check_all_errors, is_number, FormatError


def tech_part(s: str) -> float | None:
    """Создаёт и обрабатывает стек с токенами.

    Args:
        s: str

    Returns:
        float: Результат всех вычислений
    """
    tokens = get_tokens(s)
    if check_all_errors(tokens):
        stack = []
        for symbol in tokens:
            if is_number(symbol):
                stack.append(float(symbol))
            elif symbol in "+-%**//":
                if len(stack) >= 2:
                    stack.append(binary_operations(
                        symbol, stack.pop(-2), stack.pop(-1)))
                else:
                    raise FormatError("Количество операндов не соответствует количество операций")

            elif symbol in "~$":
                stack.append(unary_operations(symbol, stack.pop(-1)))

        return stack[-1]
    return None
