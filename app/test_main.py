from typing import Any

import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture
def mock_rate() -> Any:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_func:
        yield mock_func


@pytest.mark.parametrize(
    "prediction, current, expected",
    [
        pytest.param(245, 218, "Buy more cryptocurrency", id="rate > 1.05"),
        pytest.param(246, 246, "Do nothing", id="rate == 1"),
        pytest.param(245, 245, "Do nothing", id="rate == 1"),
        pytest.param(100, 100, "Do nothing", id="rate == 1"),
        pytest.param(95, 100, "Do nothing", id="rate == 0.95 boundary case"),
        pytest.param(105, 100, "Do nothing", id="rate == 1.05 boundary case"),
        pytest.param(90, 100, "Sell all your cryptocurrency",
                     id="rate < 0.95"),
        pytest.param(110, 100, "Buy more cryptocurrency", id="rate > 1.05")
    ],
)
def test_cryptocurrency_action(mock_rate: Any,
                               prediction: int,
                               current: int,
                               expected: str) -> None:
    mock_rate.return_value = prediction
    assert cryptocurrency_action(current) == expected
    mock_rate.assert_called_once_with(current)
