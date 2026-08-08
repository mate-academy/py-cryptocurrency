from unittest.mock import patch, MagicMock

import pytest

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_cryptocurrency_action_do_nothing_when_105(
        mock_prediction: MagicMock
) -> None:
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=95)
def test_cryptocurrency_action_do_nothing_when_095(
        mock_prediction: MagicMock
) -> None:
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=5)
def test_cryptocurrency_action_sell_all_your_cryptocurrency(
        mock_prediction: MagicMock
) -> None:
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=20)
def test_cryptocurrency_action_buy_more_cryptocurrency(
        mock_prediction: MagicMock
) -> None:
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=0)
def test_cryptocurrency_action_zero_prediction(
        mock_prediction: MagicMock
) -> None:
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=10)
def test_cryptocurrency_action_zero_current_rate(
        mock_prediction: MagicMock
) -> None:
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)


@patch("app.main.get_exchange_rate_prediction", return_value=0)
def test_cryptocurrency_action_both_zero(
        mock_prediction: MagicMock
) -> None:
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)
