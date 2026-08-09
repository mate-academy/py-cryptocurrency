from unittest import mock
from typing import Union, Any
import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_get_exchange_rate_prediction() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_prediction:
        yield mock_prediction


@pytest.mark.parametrize(
    "current_rate,predicate_value,expect_value",
    [
        (10.45, 20, "Buy more cryptocurrency"),
        (10, 8, "Sell all your cryptocurrency"),
        (10, 10.5, "Do nothing"),
        (10, 9.5, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
    current_rate: Union[int, float],
    predicate_value: float,
    expect_value: float,
    mock_get_exchange_rate_prediction: Any
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicate_value
    assert cryptocurrency_action(current_rate) == expect_value
