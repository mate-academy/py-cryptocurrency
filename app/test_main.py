from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction", return_value=56)
def test_buy_more(mock_prediction: MagicMock) -> None:
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"
    mock_prediction.assert_called_once()


@patch("app.main.get_exchange_rate_prediction", return_value=150)
def test_sell_all(mock_prediction: MagicMock) -> None:
    assert cryptocurrency_action(210) == "Sell all your cryptocurrency"
    mock_prediction.assert_called_once()


@patch("app.main.get_exchange_rate_prediction", return_value=235)
def test_do_nothing(mock_prediction: MagicMock) -> None:
    assert cryptocurrency_action(229) == "Do nothing"
    mock_prediction.assert_called_once()


@patch("app.main.get_exchange_rate_prediction", return_value=95)
def test_edge_case_1(mock_prediction: MagicMock) -> None:
    assert cryptocurrency_action(100) == "Do nothing"
    mock_prediction.assert_called_once()


@patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_edge_case_2(mock_prediction: MagicMock) -> None:
    assert cryptocurrency_action(100) == "Do nothing"
    mock_prediction.assert_called_once()
