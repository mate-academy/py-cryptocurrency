from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected",
    [
        (6.31, 6, "Buy more cryptocurrency"),
        (4.2, 4, "Do nothing"),
        (2.85, 3, "Do nothing"),
        (5, 5, "Do nothing"),
        (3.8, 4, "Do nothing"),
        (7.5, 8, "Sell all your cryptocurrency"),
        (-9, 3.3, "Sell all your cryptocurrency"),

    ]

)
def test_cryptocurrency_action(
        prediction_rate: int | float,
        current_rate: int | float,
        expected: int | float) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected
