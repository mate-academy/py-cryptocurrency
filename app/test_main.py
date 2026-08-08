from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_goes_right(mocked_prediction: float) -> None:
    mocked_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"

    mocked_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"

    mocked_prediction.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"

    mocked_prediction.return_value = 102
    assert cryptocurrency_action(100) == "Do nothing"

    mocked_prediction.return_value = 98
    assert cryptocurrency_action(100) == "Do nothing"

    mocked_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
