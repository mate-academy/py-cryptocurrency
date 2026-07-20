from unittest.mock import patch

import app.main


def test_do_nothing() -> None:
    current_rate = 100
    with patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = 105
        result = app.main.cryptocurrency_action(current_rate)
        assert result == "Do nothing"


def test_buy() -> None:
    current_rate = 100
    with patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = 106
        result = app.main.cryptocurrency_action(current_rate)
        assert result == "Buy more cryptocurrency"


def test_sell() -> None:
    current_rate = 100
    with patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = 94
        result = app.main.cryptocurrency_action(current_rate)
        assert result == "Sell all your cryptocurrency"


def test_do_nothing_v2() -> None:
    current_rate = 100
    with patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = 95
        result = app.main.cryptocurrency_action(current_rate)
        assert result == "Do nothing"
