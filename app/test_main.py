from unittest import mock
from app.main import cryptocurrency_action


def test_forecast_above_current_by_5_percent() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 123.45
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_forecast_below_current_by_5_percent() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 93.46
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


def test_forecast_above_or_below_5_percent_or_less() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 101.65
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_forecast_above_or_below_5_percent() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 98.55
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_forecast_is_exactly_5_percent_less() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 95
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_forecast_is_exactly_5_percent_more() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 105
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
