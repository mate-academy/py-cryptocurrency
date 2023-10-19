from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=6.25)
def test_if_exchange_rate_eq_6_25(
        mocked_rate: float) -> None:
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=4)
def test_if_exchange_rate_eq_4(
        mocked_rate: float) -> None:
    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=5.25)
def test_if_exchange_rate_eq_5_25(
        mocked_rate: float) -> None:
    assert cryptocurrency_action(5) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=4.75)
def test_if_exchange_rate_eq_4_75(
        mocked_rate: float) -> None:
    assert cryptocurrency_action(5) == "Do nothing"
