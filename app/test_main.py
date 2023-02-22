from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        yield mock_predict


def test_prediction_more_than_5_higher(mocked_rate_prediction: object) -> None:
    mocked_rate_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_prediction_less_than_5_higher(mocked_rate_prediction: object) -> None:
    mocked_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


def test_prediction_less_than_5_lower(mocked_rate_prediction: object) -> None:
    mocked_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


def test_prediction_more_than_5_lower(mocked_rate_prediction: object) -> None:
    mocked_rate_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
