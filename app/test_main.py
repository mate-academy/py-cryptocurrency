from unittest import mock

from app.main import cryptocurrency_action


def test_exchange_rate_more_5_percent_higher() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as prediction_mocked:
        prediction_mocked.return_value = 1.1
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_exchange_rate_more_5_percent_lower() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as prediction_mocked:
        prediction_mocked.return_value = 0.8
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_exchange_rate_less_then_5_percent_higher() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as prediction_mocked:
        prediction_mocked.return_value = 1.01
        assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_less_then_5_percent_lower(
        prediction_mocked: mock
) -> None:
    prediction_mocked.return_value = 0.99
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_is_the_same(prediction_mocked: mock) -> None:
    prediction_mocked.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


def test_exchange_rate_5_percent_higher() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as prediction_mocked:
        prediction_mocked.return_value = 1.05
        assert cryptocurrency_action(1) == "Do nothing"


def test_exchange_rate_5_percent_lower() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as prediction_mocked:
        prediction_mocked.return_value = 0.95
        assert cryptocurrency_action(1) == "Do nothing"
