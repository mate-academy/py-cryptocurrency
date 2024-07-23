import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction,rate",
    [
        (100, 100, "Do nothing"),
        (100, 96, "Do nothing"),
        (10000, 9500, "Do nothing"),
        (1000, 900, "Sell all your cryptocurrency"),
        (100, 103, "Do nothing"),
        (10, 10.5, "Do nothing"),
        (1000, 1120, "Buy more cryptocurrency"),
    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        prediction: int | float,
        rate: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_rate_prediction):
        mocked_get_rate_prediction.return_value = prediction
        assert cryptocurrency_action(current_rate) == rate
