from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_suggested_actions_in_predicted_exchange_rate_windows(
        mocked_prediction):
    mocked_prediction.return_value = 100

    assert cryptocurrency_action(102) == "Do nothing"
    assert cryptocurrency_action(104) == "Do nothing"
    assert cryptocurrency_action(96) == "Do nothing"
    assert cryptocurrency_action(118) == "Sell all your cryptocurrency"
    assert cryptocurrency_action(143) == "Sell all your cryptocurrency"
    assert cryptocurrency_action(123) == "Sell all your cryptocurrency"
    assert cryptocurrency_action(90) == "Buy more cryptocurrency"
    assert cryptocurrency_action(75) == "Buy more cryptocurrency"
    assert cryptocurrency_action(23) == "Buy more cryptocurrency"

