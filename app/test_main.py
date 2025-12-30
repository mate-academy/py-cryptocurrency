import pytest
from unittest import mock
from app.main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize(
    "prediction, current_rate, expected_result",
    [
        (11.44, 13, "Sell all your cryptocurrency"),
        (115.65, 100, "Buy more cryptocurrency"),
        (1.02, 1, "Do nothing"),
        (23.75, 25, "Do nothing"),
        (42, 40, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate: mock.Mock,
        prediction: Union[int | float],
        current_rate: Union[int | float],
        expected_result: str
) -> None:

    mocked_exchange_rate.return_value = prediction
    assert (cryptocurrency_action(current_rate)
            == expected_result)
