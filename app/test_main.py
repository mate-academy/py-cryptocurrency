from unittest import mock

from app.main import cryptocurrency_action


def test_cryptocurrency_action_increase_in_limits() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 78.92
        assert cryptocurrency_action(75.17) == "Do nothing"


def test_cryptocurrency_action_increase_over() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 78.93
        assert cryptocurrency_action(75.17) == "Buy more cryptocurrency"


def test_cryptocurrency_action_increase_equal_105() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 110.25
        assert cryptocurrency_action(105) == "Do nothing"


def test_cryptocurrency_action_decrease_in_limits() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 71.42
        assert cryptocurrency_action(75.17) == "Do nothing"


def test_cryptocurrency_action_decrease_lower() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 71.41
        assert cryptocurrency_action(75.17) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_decrease_equal_95() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 190
        assert cryptocurrency_action(200) == "Do nothing"
