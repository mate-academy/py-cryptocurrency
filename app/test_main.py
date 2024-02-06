import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "value,result",
    [
        (1.45, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (0.96, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_func: mock,
                               value: float,
                               result: str) -> None:
    mocked_func.return_value = value
    assert cryptocurrency_action(1.4) == result
