import pytest

from unittest import mock
from typing import Any

from app.main import cryptocurrency_action


@pytest.fixture
def fixture_mock_get() -> Any:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_get:
        yield mock_get


def test_correct_function_using(fixture_mock_get: mock.MagicMock) -> None:
    fixture_mock_get(1)
    fixture_mock_get.assert_called_once_with(1)


@pytest.mark.parametrize(
    "current_rate, exchange_rate, expected",
    [
        pytest.param(1, 0.57, "Sell all your cryptocurrency", id="1 >> 0,57"),
        pytest.param(1, 0.94, "Sell all your cryptocurrency", id="1 >> 0,94"),
        pytest.param(1, 0.95, "Do nothing", id="1 > 0,95"),
        pytest.param(1, 1.05, "Do nothing", id="1 < 1,05"),
        pytest.param(1, 1.06, "Buy more cryptocurrency", id="1 << 1,06"),
        pytest.param(1, 1.54, "Buy more cryptocurrency", id="1 << 1,54"),
    ]
)
def test_valid_prediction(
        current_rate: float | int,
        exchange_rate: float | int,
        expected: str,
        fixture_mock_get: mock.MagicMock,
) -> None:
    fixture_mock_get.return_value = exchange_rate
    fixture_mock_get(current_rate)
    assert cryptocurrency_action(current_rate) == expected
