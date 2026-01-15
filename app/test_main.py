from unittest.mock import patch

import app.main as main


def test_buy_more_cryptocurrency_when_prediction_above_105_percent() -> None:
    current_rate: float = 100.0
    predicted_rate: float = 106.0  # 106%

    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate,
    ):
        result: str = main.cryptocurrency_action(current_rate)

        assert result == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency_when_prediction_below_95_percent() -> None:
    current_rate: float = 100.0
    predicted_rate: float = 94.0  # 94%

    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate,
    ):
        result: str = main.cryptocurrency_action(current_rate)

        assert result == "Sell all your cryptocurrency"


def test_do_nothing_when_prediction_between_95_and_105_percent() -> None:
    current_rate: float = 100.0
    predicted_rate: float = 102.0

    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate,
    ):
        result: str = main.cryptocurrency_action(current_rate)

        assert result == "Do nothing"


def test_do_nothing_when_prediction_is_exactly_95_percent() -> None:
    current_rate: float = 100.0
    predicted_rate: float = 95.0  # exatamente 0.95

    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate,
    ):
        result: str = main.cryptocurrency_action(current_rate)

        assert result == "Do nothing"


def test_do_nothing_when_prediction_is_exactly_105_percent() -> None:
    current_rate: float = 100.0
    predicted_rate: float = 105.0  # exatamente 1.05

    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate,
    ):
        result: str = main.cryptocurrency_action(current_rate)

        assert result == "Do nothing"
