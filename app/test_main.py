import pytest
from unittest import mock
from unittest.mock import MagicMock

import app.main


@pytest.mark.parametrize("return_change,expected",
                         [(1.06, "Buy more cryptocurrency"),
                          (1.5, "Buy more cryptocurrency"),
                          (2.25, "Buy more cryptocurrency")])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_currency_buy(
        mocked_prediction: MagicMock,
        return_change: float | int,
        expected: str) -> None:
    mocked_prediction.return_value = return_change

    result = app.main.cryptocurrency_action(1)

    assert result == expected


@pytest.mark.parametrize("return_change,expected",
                         [(0.94, "Sell all your cryptocurrency"),
                          (0.53, "Sell all your cryptocurrency"),
                          (0.15, "Sell all your cryptocurrency")])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_currency_sell(
        mocked_prediction: MagicMock,
        return_change: float | int,
        expected: str) -> None:
    mocked_prediction.return_value = return_change

    result = app.main.cryptocurrency_action(1)

    assert result == expected


@pytest.mark.parametrize("return_change,expected",
                         [(0.95, "Do nothing"),
                          (1.05, "Do nothing")])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_currency_nothing(
        mocked_prediction: MagicMock,
        return_change: float | int,
        expected: str) -> None:
    mocked_prediction.return_value = return_change

    result = app.main.cryptocurrency_action(1)

    assert result == expected
