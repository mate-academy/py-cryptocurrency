from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 106  # > 5% acima de 100
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 94  # > 5% abaixo de 100
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_difference_is_small(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 102  # dentro da faixa de ±5%
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_is_exactly_105_percent(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 105.0  # exatamente 5% acima
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_is_exactly_95_percent(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 95.0  # exatamente 5% abaixo
    assert cryptocurrency_action(100) == "Do nothing"
