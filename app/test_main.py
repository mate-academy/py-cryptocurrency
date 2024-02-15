import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "value,result",
    [
        (1.25, "Buy more cryptocurrency"),
        (0.88, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
        (1.05, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_func: mock,
                               value: float,
                               result: str) -> None:
    mocked_func.return_value = value
    assert cryptocurrency_action(1) == result
