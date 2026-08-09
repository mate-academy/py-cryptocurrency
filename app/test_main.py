from typing import Any

from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange_prediction() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_rate_prediction:
        yield mock_rate_prediction


@pytest.mark.parametrize(
    "digit,expected_result",
    [
        pytest.param(105, "Do nothing"),
        pytest.param(95, "Do nothing"),
        pytest.param(93, "Sell all your cryptocurrency"),
        pytest.param(107, "Buy more cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        mocked_exchange_prediction: Any,
        digit: int,
        expected_result: str
) -> None:
    mocked_exchange_prediction.return_value = digit

    assert cryptocurrency_action(100) == expected_result
