from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mock_value, expected_value, message",
    [
        (1000, 100, "Buy more cryptocurrency"),
        (94, 100, "Sell all your cryptocurrency"),
        (103, 100, "Do nothing")
    ]
)
def test_buy_more_crypto(mock_value: int,
                         expected_value: int,
                         message: str) -> None:
    with patch("app.main.get_exchange_rate_prediction") as rate:
        rate.return_value = mock_value
        assert cryptocurrency_action(expected_value) == message


def test_rate_95_percent_do_nothing():
    with patch('app.main.get_exchange_rate_prediction', return_value=95):  # Пример значения для 0.95 границы
        assert cryptocurrency_action(100) == "Do nothing"


def test_rate_105_percent_do_nothing():
    with patch('app.main.get_exchange_rate_prediction', return_value=105):  # Пример значения для 1.05 границы
        assert cryptocurrency_action(100) == "Do nothing"
