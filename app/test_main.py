from typing import Any

import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.fixture()
def mocked_exchange_rate() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_exchange_rate:
        yield mock_exchange_rate


@pytest.mark.parametrize(
    "digit,expected_result",
    [
        pytest.param(105, "Do nothing"),
        pytest.param(95, "Do nothing"),
        pytest.param(94, "Sell all your cryptocurrency"),
        pytest.param(106, "Buy more cryptocurrency")
    ]
)
def test_cryptocurrency_action(mocked_exchange_rate: Any,
                               digit: int,
                               expected_result: str) -> None:
    mocked_exchange_rate.return_value = digit

    assert cryptocurrency_action(100) == expected_result
