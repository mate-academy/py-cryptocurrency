from unittest import mock
from app.main import cryptocurrency_action


def test_for_buy_cryptocurrency() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = 106
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_for_sell_cryptocurrency() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = 94
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_for_do_nothing_with_cryptocurrency_float_number1() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = 105.0
        assert cryptocurrency_action(100.0) == "Do nothing"


def test_for_do_nothing_with_cryptocurrency_float_number2() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = 100.0
        assert cryptocurrency_action(104.0) == "Do nothing"


def test_for_do_nothing_with_cryptocurrency_float_number3() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = 99.0
        assert cryptocurrency_action(95.0) == "Do nothing"
