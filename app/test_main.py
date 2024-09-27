from __future__ import annotations
from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate_predict() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predictin:
        yield mock_predictin


def test_rate_more_than_current(mocked_rate_predict: str) -> None:
    mocked_rate_predict.return_value = 15
    assert cryptocurrency_action(12) == "Buy more cryptocurrency"


def test_rate_less_than_current(mocked_rate_predict: str) -> None:
    mocked_rate_predict.return_value = 12
    assert cryptocurrency_action(15) == "Sell all your cryptocurrency"


def test_rate_almost_equel_than_current(mocked_rate_predict: str) -> None:
    mocked_rate_predict.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


def test_rate_almost_equel_than_current_1(mocked_rate_predict: str) -> None:
    mocked_rate_predict.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
