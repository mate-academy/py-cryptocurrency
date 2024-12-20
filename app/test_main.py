import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize (
    "current_rate, prediction_rate, expected",
    [
        (10, 10.0, "Do nothing"),
        (10, 10.5, "Do nothing"),
        (10, 9.5, "Do nothing"),
        (10, 15.0, "Buy more cryptocurrency"),
        (10, 5.0, "Sell all your cryptocurrency"),
    ]
)

@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_rate: mock.MagicMock,
              current_rate: int,
              prediction_rate: float,
              expected: str
              ) -> None:

    mock_rate.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected