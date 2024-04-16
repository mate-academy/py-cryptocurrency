import pytest

from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "current_rate,fake_predict,result",
    [
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
    ],
)
def test_action(
    current_rate: int | float,
    fake_predict: int | float,
    result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked:
        mocked.return_value = fake_predict
        assert cryptocurrency_action(current_rate) == result
