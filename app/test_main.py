from app.main import cryptocurrency_action

from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_your_cryptocurrency(random_mock: mock) -> None:
    random_mock.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_0_95(random_mock: mock) -> None:
    random_mock.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_1_05(random_mock: mock) -> None:
    random_mock.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(random_mock: mock) -> None:
    random_mock.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"
