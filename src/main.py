from src.calculator import tech_part


def main() -> None:
    """
    Основная функция работы калькулятора.
    Получает выражение от пользователя, вычисляет его и выводит результат
    """
    s = str(input())
    answer = tech_part(s)
    if answer is not None:
        print(answer)


if __name__ == "__main__":
    main()
