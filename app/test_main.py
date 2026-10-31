from unittest import mock

import pytest

from app import main


@pytest.mark.parametrize(
    "prediction_rate,expected",
    [
        (110, "Buy more cryptocurrency"),
        (105.01, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (100, "Do nothing"),
        (95, "Do nothing"),
        (94.99, "Sell all your cryptocurrency"),
        (90, "Sell all your cryptocurrency"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_prediction: mock.MagicMock,
    prediction_rate: float,
    expected: str,
) -> None:
    mocked_prediction.return_value = prediction_rate
    assert main.cryptocurrency_action(100) == expected
