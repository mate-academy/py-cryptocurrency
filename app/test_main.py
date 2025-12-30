import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,result",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        prediction_rate: int,
        current_rate: int,
        result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        mocked_rate.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == result
