from unittest import mock
from app.main import get_exchange_rate_prediction
from app.main import cryptocurrency_action


def test_should_return_string() -> None:
    assert isinstance(cryptocurrency_action(1), str)


def test_get_exchange_rate_prediction_return_float() -> None:
    assert isinstance(get_exchange_rate_prediction(2), float)


def test_get_exchange_rate_prediction_return_0_when_get_0() -> None:
    assert get_exchange_rate_prediction(0) == 0


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_more(mock_func: float) -> None:
    mock_func.return_value = 2.2
    assert cryptocurrency_action(2) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell_all(mock_func: float) -> None:
    mock_func.return_value = 1.8
    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_return_do_nothing_when_correlation_is_105(mock_func: float) -> None:
    mock_func.return_value = 2.1
    assert cryptocurrency_action(2) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_return_do_nothing_when_correlation_is_095(mock_func: float) -> None:
    mock_func.return_value = 1.9
    assert cryptocurrency_action(2) == "Do nothing"
