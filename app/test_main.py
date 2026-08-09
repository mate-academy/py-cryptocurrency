from typing import Union
from unittest.mock import MagicMock, patch

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate",
    [
        (100, 105.1),
        (100, 105.8),
        (100, 106.0),
        (100, 106.5),
        (100, 200),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_should_buy_when_predicted_rate_five_percent_higher(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: Union[int, float],
        prediction_rate: float,
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@pytest.mark.parametrize(
    "current_rate,prediction_rate",
    [
        (100, 1),
        (100, 90.5),
        (100, 94.0),
        (100, 94.9),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_should_sell_when_predicted_rate_five_percent_lower(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: Union[int, float],
        prediction_rate: float,
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert (
        cryptocurrency_action(current_rate) == "Sell all your cryptocurrency"
    ), (
        "Should sell when predicted rate 5% lower than current"
    )


@pytest.mark.parametrize(
    "current_rate,prediction_rate",
    [
        (100, 95.0),
        (100, 96.0),
        (100, 100.0),
        (100, 104.5),
        (100, 105.0),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_predicted_rate_within_five_percent(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: Union[int, float],
        prediction_rate: float,
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == "Do nothing"
