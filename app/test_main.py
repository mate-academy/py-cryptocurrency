from unittest import mock
from app.main import cryptocurrency_action


def test_print_buy_more() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=11.37) as mock_prediction:
        result = cryptocurrency_action(5)

        mock_prediction.assert_called_once()
        assert result == "Buy more cryptocurrency"


def test_print_sell_all() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=3.14) as mock_prediction:
        result = cryptocurrency_action(15)

        mock_prediction.assert_called_once()
        assert result == "Sell all your cryptocurrency"


def test_print_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=10) as mock_prediction:
        result = cryptocurrency_action(9.6)

        mock_prediction.assert_called_once()
        assert result == "Do nothing"
