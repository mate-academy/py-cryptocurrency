import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, current_rate, expected",
    [
        pytest.param(0.90, 1, "Sell all your cryptocurrency"),
        pytest.param(0.95, 1, "Do nothing"),
        pytest.param(0.99, 1, "Do nothing"),
        pytest.param(1.05, 1, "Do nothing"),
        pytest.param(1.10, 1, "Buy more cryptocurrency")
    ],
    ids=[
        "Bad investment scenario",
        "You should wait",
        "You should wait",
        "You should wait",
        "It's time to buy"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_rate_prediction: mock.Mock,
        prediction: float,
        current_rate: int,
        expected: str
) -> None:
    mocked_rate_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected
