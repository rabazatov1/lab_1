import pytest
from src.calculator import tech_part
from src.errors import FormatError, BracketsError


def test_all_operations():
    assert tech_part("4 4 +") == 8.0
    assert tech_part("10 5 -") == 5.0
    assert tech_part("6 3 *") == 18.0
    assert tech_part("5 4 /") == 1.25
    assert tech_part("15 6 %") == 3.0
    assert tech_part("7 2 //") == 3.0
    assert tech_part("3 2 **") == 9.0
    assert tech_part("3 $") == 3.0
    assert tech_part("2 ~") == -2.0


def test_single_numbers():
    assert tech_part("12") == 12.0


def test_combination_operations():
    assert tech_part("3 5 + 7 *") == 56.0
    assert tech_part("3 $ 5 ** 7 //") == 34.0
    assert tech_part("3 2 - 6 * 4 % 15 +") == 17.0


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
        tech_part('')


def test_correct_symbols():
    with pytest.raises(SyntaxError):
        assert tech_part('2 a *')


def test_operands_must_be_integer():
    with pytest.raises(ValueError):
        tech_part('2.4 5 //')
    with pytest.raises(ValueError):
        tech_part('5 8.9 %')


def test_correct_brackets():
    with pytest.raises(BracketsError):
        assert tech_part('( 2 5 +')
    with pytest.raises(BracketsError):
        assert tech_part('( 6 7 ) +')
    with pytest.raises(BracketsError):
        assert tech_part('4 (2 5+ -)')
