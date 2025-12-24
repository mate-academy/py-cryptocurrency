from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_increase_rate(mocked_prediction: mock.MagicMock) -> None:
    mocked_prediction.return_value = 12
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_decrease_rate_but_lesser_than_braking_point(
    mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_decrease_rate(mocked_prediction: mock.MagicMock) -> None:
    mocked_prediction.return_value = 9.4
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_increase_rate_but_lesser_than_braking_point(
    mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_the_same(mocked_prediction: mock.MagicMock) -> None:
    mocked_prediction.return_value = 10
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_zero(mocked_prediction: mock.MagicMock) -> None:
    mocked_prediction.return_value = 0
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"
