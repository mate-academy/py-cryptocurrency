from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


def test_if_the_forecast_rate_is_by_5_percent_lower(
        mocked_exchange_rate_prediction: pytest.fixture
) -> None:
    mocked_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_if_the_forecast_rate_is_exceeded_by_5_percent(
        mocked_exchange_rate_prediction: pytest.fixture
) -> None:
    mocked_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_if_the_forecast_rate_is_not_exceeded_by_5_percent(
        mocked_exchange_rate_prediction: pytest.fixture
) -> None:
    mocked_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_if_the_forecast_rate_is_not_less_5_percent(
        mocked_exchange_rate_prediction: pytest.fixture
) -> None:
    mocked_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
