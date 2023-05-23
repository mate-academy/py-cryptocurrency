from unittest import mock

from app.main import cryptocurrency_action


def test_function_was_called() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 1.2
        cryptocurrency_action(2)
        mocked_prediction.assert_called_with(2)


def test_if_difference_less_than_5_perc() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 0.95
        assert cryptocurrency_action(1) == "Do nothing"
        mocked_prediction.return_value = 1.05
        assert cryptocurrency_action(1) == "Do nothing"


def test_if_difference_more_than_5_perc() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 0.9
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
        mocked_prediction.return_value = 1.5
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"
