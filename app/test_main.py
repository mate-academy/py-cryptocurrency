from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_called(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1
    cryptocurrency_action(1)
    mock_get_exchange_rate_prediction.assert_called_with(1)


@pytest.mark.parametrize(
    "current_rate, prediction_rate",
    [
        (1.3, 1.37),
        (1.5, 2),
        (2, 2.12),
        (3.04, 3.21),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_rate_much_greater_than_current(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: float | int,
        prediction_rate: float | int,
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@pytest.mark.parametrize(
    "current_rate, prediction_rate",
    [
        (1.37, 1.3),
        (2, 1.5),
        (2.12, 2),
        (3.21, 3.04),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_rate_much_less_than_current(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: float | int,
        prediction_rate: float | int,
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert (cryptocurrency_action(current_rate)
            == "Sell all your cryptocurrency")


@pytest.mark.parametrize(
    "current_rate, prediction_rate",
    [
        (1, 1),
        (2, 2.1),
        (1.5, 1.45),
        (3.2, 3.04),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_rate_approximately_equal_to_current(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: float | int,
        prediction_rate: float | int,
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == "Do nothing"
