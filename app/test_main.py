import pytest

from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, current_rate, expected",
    [
        (130, 80, "Buy more cryptocurrency"),
        (90, 120, "Sell all your cryptocurrency"),
        (101, 102, "Do nothing"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_can_access_google_page(
        mock_get_exchange_rate_prediction: None,
        prediction: int | float,
        current_rate: int | float,
        expected: str
) -> None:

    mock_get_exchange_rate_prediction.return_value = prediction

    assert cryptocurrency_action(current_rate) == expected
