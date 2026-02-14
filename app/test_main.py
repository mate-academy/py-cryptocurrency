from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_ratio_is_greater_than_1_05(
        mocked_get_exchange_rate_prediction: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.06
    current_rate = 1
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_ratio_is_less_than_0_95(
        mocked_get_exchange_rate_prediction: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.94
    current_rate = 1
    assert (cryptocurrency_action(current_rate)
            == "Sell all your cryptocurrency")


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_ratio_is_equal_to_0_95(
        mocked_get_exchange_rate_prediction: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    current_rate = 1
    assert cryptocurrency_action(current_rate) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_ratio_is_equal_to_1_05(
        mocked_get_exchange_rate_prediction: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    current_rate = 1
    assert cryptocurrency_action(current_rate) == "Do nothing"
