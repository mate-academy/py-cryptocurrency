from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_should_buy(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_sell(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 102
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_at_105(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 105.0  # рівно 5% вище
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_at_95(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 95.0  # рівно 5% нижче
    assert cryptocurrency_action(100) == "Do nothing"
