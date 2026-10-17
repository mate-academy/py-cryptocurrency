from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_buy_when_rate_up(
        mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 1.06
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_rate_up_for_5_percent(
        mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_rate_down_for_5_percent(
        mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_sell_when_rate_down(
        mocked_prediction: mock.MagicMock
) -> None:
    mocked_prediction.return_value = 0.94
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"
