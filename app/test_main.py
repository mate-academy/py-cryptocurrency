from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_exchange_rate_prediction() -> mock.Mock:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_rate_prediction:
        yield mock_rate_prediction


@pytest.mark.parametrize(
    "current_rate,prediction_rate,result",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency")
    ],
    ids=[
        "Predicted rate higher 1.05",
        "Predicted rate equal to 1.05",
        "Predicted rate equal to 0.95",
        "Predicted rate less 0.95"
    ]
)
def test_cryptocurrency(
        mock_exchange_rate_prediction: mock.Mock,
        current_rate: int,
        prediction_rate: int,
        result: str
) -> None:
    mock_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
