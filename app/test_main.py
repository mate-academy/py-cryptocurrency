from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 0.94, "Sell all your cryptocurrency"),
    ]
)
def test_func_should_return_correct_values_in_boundary_cases(
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str
) -> None:
    with (
        mock.patch("app.main.get_exchange_rate_prediction",
                   return_value=prediction_rate)
    ):
        assert cryptocurrency_action(current_rate) == expected


@pytest.mark.parametrize(
    "argument, expected_error",
    [
        ("str", TypeError),
        (0, ZeroDivisionError)
    ]
)
def test_func_should_raise_correct_error(
        argument: any,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        cryptocurrency_action(argument)
