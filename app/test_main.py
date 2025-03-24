from app.main import cryptocurrency_action
import pytest
from unittest import mock


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_test:
        yield mock_test


def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: int | float
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.9
    result = cryptocurrency_action(1.06)
    assert result == "Do nothing"

    mocked_get_exchange_rate_prediction.return_value = 1.9
    result = cryptocurrency_action(1.11)
    assert result == "Buy more cryptocurrency"

    mocked_get_exchange_rate_prediction.return_value = 0.94
    result = cryptocurrency_action(1)
    assert result == "Sell all your cryptocurrency"
