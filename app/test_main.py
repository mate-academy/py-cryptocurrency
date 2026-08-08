import pytest
from unittest import mock
from typing import Union

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "exchange_rate,current_rate,expected_result",
    [
        pytest.param(
            1,
            1,
            "Do nothing",
            id="current rate and rate prediction are equal"
        ),
        pytest.param(
            0.95,
            1,
            "Do nothing",
            id="do nothing if rate from 0.95 to 1.05"
        ),
        pytest.param(
            1.05,
            1,
            "Do nothing",
            id="do nothing if rate from 0.95 to 1.05"
        ),
        pytest.param(
            2,
            1,
            "Buy more cryptocurrency",
            id="prediction rate more than current rate"
        ),
        pytest.param(
            0.5,
            1,
            "Sell all your cryptocurrency",
            id="prediction rate less than current rate"
        ),
        (
            100,
            75,
            "Buy more cryptocurrency",
        ),
        (
            22.2,
            85,
            "Sell all your cryptocurrency",
        ),
        (
            -10,
            -5,
            "Buy more cryptocurrency",
        ),
        (
            -24.6,
            -106.4,
            "Sell all your cryptocurrency",
        ),
    ]
)
def test_cryptocurrency_action(
        mocked_rate_prediction: any,
        exchange_rate: Union[int, float],
        current_rate: Union[int, float],
        expected_result: str
) -> None:
    mocked_rate_prediction.return_value = exchange_rate

    assert cryptocurrency_action(current_rate) == expected_result


@pytest.mark.parametrize(
    "initial_element,expected_error",
    [
        pytest.param(
            0,
            ZeroDivisionError,
            id="zero is not a valid rate"
        ),
        pytest.param(
            "14",
            TypeError,
            id="string is not valid rate, should int or float"
        ),
        pytest.param(
            [],
            TypeError,
            id="list is not valid rate, should int or float"
        )
    ]
)
def test_should_return_error_correctly(
        initial_element: any,
        expected_error: EOFError
) -> None:
    with pytest.raises(expected_error):
        cryptocurrency_action(initial_element)
