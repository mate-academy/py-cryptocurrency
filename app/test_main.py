import pytest
from unittest import mock


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (0.95, 1, "Do nothing"),
        (1.05, 1, "Do nothing"),
        (0.93, 1, "Sell all your cryptocurrency"),
        (1.07, 1, "Buy more cryptocurrency")
    ],
    ids=[
        "Should return 'Do nothing' if prediction_rate == 0.95",
        "Should return 'Do nothing' if prediction_rate == 1.05",
        "Should return 'Sell all your cryptocurrency'if prediction_rate==0.93",
        "Should return 'Buy more cryptocurrency' if prediction_rate == 1.07",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_predict_expected_cryptocurrency_actions(
        mocked_prediction_rate: mock,
        prediction_rate: float,
        current_rate: int,
        expected_result: str
) -> None:
    mocked_prediction_rate.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected_result
