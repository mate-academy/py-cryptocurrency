import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (0.95, 1, "Do nothing"),
        (1.05, 1, "Do nothing"),
        (0.90, 1, "Sell all your cryptocurrency"),
        (1.10, 1, "Buy more cryptocurrency")
    ],
    ids=[
        "Return 'Do nothing' if prediction_rate == 0.95",
        "Return 'Do nothing' if prediction_rate == 1.05",
        "Return 'Sell all your cryptocurrency' if prediction_rate==0.90",
        "Return 'Buy more cryptocurrency' if prediction_rate == 1.10",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_predict_cryptocurrency_actions(
        mocked_prediction_rate: mock.MagicMock(),
        prediction_rate: float,
        current_rate: int,
        expected_result: str
) -> None:
    mocked_prediction_rate.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected_result
