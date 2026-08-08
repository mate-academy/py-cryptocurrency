from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_when_rate_increases_significantly(
    predict_mock: mock.MagicMock
) -> None:
    predict_mock.return_value = 110.0
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell_when_rate_drops_significantly(
    predict_mock: mock.MagicMock
) -> None:
    predict_mock.return_value = 80.0
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_rate_is_exactly_five_percent_higher(
    predict_mock: mock.MagicMock
) -> None:
    predict_mock.return_value = 105.0
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_rate_is_exactly_five_percent_lower(
    predict_mock: mock.MagicMock
) -> None:
    predict_mock.return_value = 95.0
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_rate_stays_same(
    predict_mock: mock.MagicMock
) -> None:
    predict_mock.return_value = 50.0
    result = cryptocurrency_action(50)
    assert result == "Do nothing"
