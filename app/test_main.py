import pytest
from unittest import mock
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, prediction_rate, expected_result", [
    (1, 1.051, "Buy more cryptocurrency"),
    (1, 1.05, "Do nothing"),
    (1, 1, "Do nothing"),
    (1, 0.95, "Do nothing"),
    (1, 0.949, "Sell all your cryptocurrency")

])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.patch,
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result


@pytest.mark.parametrize("current_rate, prediction_rate, expected_result", [
    ("0.95", 1.051, TypeError),
    ([0.951, ""], 1, TypeError),
    (1, (1, 2), TypeError),
    (0.96, {1: 49, 2: 55}, TypeError)
])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_type(
        mock_get_exchange_rate_prediction: mock.patch,
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    with pytest.raises(expected_result):
        cryptocurrency_action(current_rate)
