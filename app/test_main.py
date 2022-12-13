from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_mocked_1_06_value(mocked_fun: mock) -> None:
    mocked_fun.return_value = 10.6
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_mocked_9_value(mocked_fun: mock) -> None:
    mocked_fun.return_value = 9
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_mocked_9_5_value(mocked_fun: mock) -> None:
    mocked_fun.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_mocked_value(mocked_fun: mock) -> None:
    mocked_fun.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"
