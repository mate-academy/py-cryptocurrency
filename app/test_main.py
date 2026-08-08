from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test__rise_prediction(mock_get_exchange_rate_prediction:
                          MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.06
    assert (cryptocurrency_action(1)
            == "Buy more cryptocurrency")


@mock.patch("app.main.get_exchange_rate_prediction")
def test__fall_prediction(mock_get_exchange_rate_prediction:
                          MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.94
    assert (cryptocurrency_action(1)
            == "Sell all your cryptocurrency")


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_exact_plus_5(mock_get_exchange_rate_prediction:
                                 MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05
    assert (cryptocurrency_action(1)
            == "Do nothing")


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_exact_minus_5(mock_get_exchange_rate_prediction:
                                  MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95
    assert (cryptocurrency_action(1)
            == "Do nothing")
