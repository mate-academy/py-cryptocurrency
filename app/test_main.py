from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_predict_rate: callable
) -> None:

    check_options = [
        (110, 100, "Buy more cryptocurrency"),
        (90, 100, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing")
    ]

    for option in check_options:
        predict_rate, current_rate, expected_tip = option

        mocked_predict_rate.return_value = predict_rate
        assert cryptocurrency_action(current_rate) == expected_tip
        mocked_predict_rate.assert_called_with(current_rate)
