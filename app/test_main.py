from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock.Mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 110
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"

    mocked_get_exchange_rate_prediction.return_value = 90
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"

    mocked_get_exchange_rate_prediction.return_value = 102
    result = cryptocurrency_action(100)
    assert result == "Do nothing"

    mocked_get_exchange_rate_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"

    mocked_get_exchange_rate_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
