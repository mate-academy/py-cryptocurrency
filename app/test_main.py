from unittest import mock
from .main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_buy_when_rate_gt_1_05(mocked_prediction: mock) -> None:
    mocked_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_not_buy_when_rate_lt_0_95(mocked_prediction: mock) -> None:
    mocked_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_ge_0_95(mocked_prediction: mock) -> None:
    mocked_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_le_1_05(mocked_prediction: mock) -> None:
    mocked_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
