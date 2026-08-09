import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, result",
    [
        (1.06, "Buy more cryptocurrency"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing"),
        (0.94, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate_prediction: mock,
        prediction: float,
        result: str
) -> None:
    mocked_exchange_rate_prediction.return_value = prediction
    assert cryptocurrency_action(1) == result
