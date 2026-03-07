from typing import Union
from unittest.mock import Mock, patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_rate_above_105_percent_buy_more(
    mock_get_exchange_rate_prediction: Mock,
) -> None:
    current_rate: Union[int, float] = 100.0
    mock_get_exchange_rate_prediction.return_value = 106.0  # 6% w górę

    result = cryptocurrency_action(current_rate)

    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_below_95_percent_sell_all(
    mock_get_exchange_rate_prediction: Mock,
) -> None:
    current_rate: Union[int, float] = 100.0
    mock_get_exchange_rate_prediction.return_value = 94.0  # 6% w dół

    result = cryptocurrency_action(current_rate)

    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_exactly_105_percent_do_nothing(
    mock_get_exchange_rate_prediction: Mock,
) -> None:
    current_rate: Union[int, float] = 100.0
    mock_get_exchange_rate_prediction.return_value = 105.0  # ratio == 1.05

    result = cryptocurrency_action(current_rate)

    assert result == "Do nothing", (
        "You should not buy cryptocurrency when "
        "prediction_rate / current_rate == 1.05"
    )


@patch("app.main.get_exchange_rate_prediction")
def test_rate_exactly_95_percent_do_nothing(
    mock_get_exchange_rate_prediction: Mock,
) -> None:
    current_rate: Union[int, float] = 100.0
    mock_get_exchange_rate_prediction.return_value = 95.0  # ratio == 0.95

    result = cryptocurrency_action(current_rate)

    assert result == "Do nothing", (
        "You should not sell cryptocurrency when "
        "prediction_rate / current_rate == 0.95"
    )
