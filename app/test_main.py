import pytest

from typing import Union

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, expected",
    [
        (900, "Sell all your cryptocurrency"),
        (1020.5, "Do nothing"),
        (1600, "Buy more cryptocurrency"),
        (1000, "Do nothing"),
        (1050, "Do nothing"),
        (950, "Do nothing"),
        (988.6, "Do nothing")
    ]
)
def test_cryptocurrency_action_should_return_expected_value(
        prediction: Union[int, float],
        expected: str,
        current_rate: Union[int, float] = 1000
) -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_get_exchange_rate:
        mocked_get_exchange_rate.return_value = prediction
        assert cryptocurrency_action(current_rate) == expected
