import pytest

from unittest import mock
from typing import Iterator
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_rate_prediction() -> Iterator[MagicMock]:
    with mock.patch("app.main.get_exchange_rate_prediction") as patched:
        yield patched


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected",
    [
        pytest.param(
            105.1,
            100,
            "Buy more cryptocurrency",
            id="test_increase_more_than_5_percent"
        ),
        pytest.param(
            105,
            100,
            "Do nothing",
            id="test_increase_less_or_equal_5_percent"
        ),
        pytest.param(
            94.9,
            100,
            "Sell all your cryptocurrency",
            id="test_decrease_more_than_5_percent"
        ),
        pytest.param(
            95,
            100,
            "Do nothing",
            id="test_decrease_less_or_equal_5_percent"
        ),
    ]
)
def test_program_working_with_different_values(
        prediction_rate: int | float,
        current_rate: int | float,
        expected: str,
        mock_rate_prediction: MagicMock
) -> None:
    mock_rate_prediction.return_value = prediction_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected
