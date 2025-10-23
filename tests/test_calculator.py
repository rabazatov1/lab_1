import pytest
from src.calculator import tech_part
from src.errors import FormatError, BracketsError


def test_all_operations():
    assert tech_part("4 4 +") == 8
    assert tech_part("10 5 -") == 5
    assert tech_part("6 3 *") == 18
    assert tech_part("5 4 /") == 1.25
    assert tech_part("15 6 %") == 3
    assert tech_part("7 2 //") == 3
    assert tech_part("3 2 **") == 9
    assert tech_part("3 $") == 3
    assert tech_part("2 ~") == -2


def test_single_numbers():
    assert tech_part("12") == 12


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        tech_part("3 0 /")
    with pytest.raises(ZeroDivisionError):
        tech_part("3 0 //")
    with pytest.raises(ZeroDivisionError):
        tech_part("3 0 %")


def test_operations_operands_balance():
    with pytest.raises(FormatError):
        assert tech_part("3 2")
    with pytest.raises(FormatError):
        assert tech_part("1 *")
    with pytest.raises(FormatError):
        assert tech_part("1 2 $")


def test_empty_line():
    with pytest.raises(ValueError):
        tech_part("")
    with pytest.raises(ValueError):
        tech_part("            ")


def test_correct_symbols():
    with pytest.raises(SyntaxError):
        assert tech_part("2 a *")
    with pytest.raises(SyntaxError):
        assert tech_part("2 5 ^")
    with pytest.raises(SyntaxError):
        assert tech_part("{6 3 *}")


def test_operands_must_be_integer():
    with pytest.raises(ValueError):
        tech_part("2.4 5 //")
    with pytest.raises(ValueError):
        tech_part("5 8.9 %")


def test_correct_brackets():
    with pytest.raises(BracketsError):
        assert tech_part("( 2 5 +")
    with pytest.raises(BracketsError):
        assert tech_part("( 6 7 ) +")
    with pytest.raises(BracketsError):
        assert tech_part("4 (2 5 + -)")


def test_negative_numbers():
    assert tech_part("5 10 ~ +") == -5
    assert tech_part("70 15 ~ //") == -5
    assert tech_part("3 ~ 2 **") == 9
    assert tech_part("8 ~ ~") == 8
    assert tech_part("3 ~ $") == -3
    assert tech_part("10 ~ 6 ~ *") == 60


def test_priority_operations():
    """3 + 4 * 2 = 11 (умножение приоритетнее)"""
    assert tech_part("3 4 2 * + ") == 11

    """10 - 6 % 4 = 10 (деление приоритетнее)"""
    assert tech_part("10 6 2 % - ") == 10

    """2 * 3 ** 2 = 18 (возведение в степень приоритетнее)"""
    assert tech_part("2 3 2 ** *") == 18

    """(2 + 3) * (8 - 3) = 25 (действия в скобках приоритетнее)"""
    assert tech_part("2 3 + 8 3 - *") == 25

    """15 // (7 - 2) * 3 = 9 (действия в скобках приоритетнее)"""
    assert tech_part("15 7 2 - / 3 *") == 9

    """((5 - 3) * 4) + (10 / 2) = 13 (действия в скобках приоритетнее)"""
    assert tech_part("5 3 - 4 * 10 2 / +") == 13

    """-5 + 3 = -2 (унарные операции приоритетнее)"""
    assert tech_part("5 ~ 3 +") == -2

    """(-7) * 4 = -28 (унарные операции приоритетнее)"""
    assert tech_part("7 4 ~ *") == -28

    """-2 ** 3 = -8 (унарные операции приоритетнее)"""
    assert tech_part("2 ~ 3 **") == -8

    """10 - 3 + 2 = 9 (левая ассоциативность)"""
    assert tech_part("10 3 - 2 +") == 9

    """20 // 4 * 2 = 10 (левая ассоциативность)"""
    assert tech_part("20 4 // 2 *") == 10

    """2 ** 3 ** 2 = 512 (правая ассоциативность)"""
    assert tech_part("2 3 2 ** **") == 512


def test_complex_expressions():
    """(((1 + 2) * 3) - 4) // 5) + 6 = 7"""
    assert tech_part("1 2 + 3 * 4 - 4 / 6 +") == 7.25

    """((2 + 3) * 4 - 5) / 3 + 2 ** 3 = 13"""
    assert tech_part("2 3 + 4 * 5 - 3 / 2 3 ** + ~") == -13

    """((10 - (2 + 3)) * 4) % 3 = 2"""
    assert tech_part("10 2 3 + - 4 * 3 %") == 2

    """-(2.5 + 3.5) * (4.2 - 1.2) / 2 = 9"""
    assert tech_part("2.5 3.5 + ~ 4.2 1.2 - * 4 /") == -4.5


def test_type_compatibility():
    assert tech_part("5 3 +") == 8
    assert tech_part("2.5 3.7 +") == 6.2
    assert tech_part("6 2.5 -") == 3.5
    assert tech_part("5.0 2.0 //") == 2
    assert tech_part("3 2.5 *") == 7.5
    assert tech_part("4 0.5 **") == 2

def test_number_of_spaces():
    assert tech_part("3    4    +    2  *") == 14
    assert tech_part("      3 4 + 2 *") == 14
    assert tech_part("3 4 + 2 *       ") == 14
    assert tech_part("      3 4 + 2 *     ") == 14
    assert tech_part("3         4         +        2      *      ") == 14
