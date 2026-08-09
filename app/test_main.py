import pytest

from unittest import mock
from app.main import cryptocurrency_action
from typing import Callable


@pytest.fixture()
def mocked_get_prediction() -> None:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
            as mock_get_prediction
    ):
        yield mock_get_prediction


@pytest.mark.parametrize(
    "prev_rate,result",
    [
        (3, "Buy more cryptocurrency"),
        (1, "Sell all your cryptocurrency"),
        (1.9, "Do nothing"),
        (2.1, "Do nothing")
    ]
)
def test_can_access_google_page(
        prev_rate: int | float,
        result: str,
        mocked_get_prediction: Callable,
) -> None:
    mocked_get_prediction.return_value = prev_rate

    assert cryptocurrency_action(2) == result
