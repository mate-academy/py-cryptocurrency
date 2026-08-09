from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_get_exchange_rate_prediction_request(
        mocked_get_exchange_rate_prediction: mock.Mock
) -> None:
    current_rate = 100
    mocked_get_exchange_rate_prediction.return_value = 106.5
    cryptocurrency_action(current_rate)
    mocked_get_exchange_rate_prediction.assert_called_once_with(current_rate)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_delta_rate_more_than_5_percent(
        mocked_get_exchange_rate_prediction: mock.Mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_delta_rate_less_than_minus_5_percent(
        mocked_get_exchange_rate_prediction: mock.Mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_delta_between_boundary_conditions(
        mocked_get_exchange_rate_prediction: mock.Mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 100
    assert cryptocurrency_action(100) == "Do nothing"
    mocked_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
    mocked_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
