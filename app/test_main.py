import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction,rate",
    [
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 105.9, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 94.5, "Sell all your cryptocurrency"),
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
