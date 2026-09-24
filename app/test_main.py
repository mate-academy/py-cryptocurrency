from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=106)
def test_should_return_buy_more_cryptocurrency(
        mock_object: mock.MagicMock
) -> None:
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=94)
def test_should_return_sell_all_your_cryptocurrency(
        mock_object: mock.MagicMock
) -> None:
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_should_return_do_nothing_with_equal_5_percent(
        mock_object: mock.MagicMock
) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=95)
def test_should_return_do_nothing_with_equal_minus_5_percent(
        mock_object: mock.MagicMock
) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
