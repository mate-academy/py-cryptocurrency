from unittest import mock
import pytest
from app import main


@pytest.mark.parametrize(
    "prediction, current, expected",
    [
        (105.1, 100, "Buy more cryptocurrency"),
        (105, 100, "Do nothing"),
        (100, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (94.9, 100, "Sell all your cryptocurrency"),
        (110, 100, "Buy more cryptocurrency"),
        (80, 100, "Sell all your cryptocurrency"),
    ]
)
def test_cryptocurrency_action(
        prediction: float,
        current: float,
        expected: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_prediction:
        mock_prediction.return_value = prediction

        result = main.cryptocurrency_action(current)

        assert result == expected
