import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected_result",
    [
        (5, 1, "Buy more cryptocurrency"),
        (1, 5, "Sell all your cryptocurrency"),
        (5, 5, "Do nothing"),
        (19, 20, "Do nothing"),
        (21, 20, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction(
        mock_exchange_rate: mock.MagicMock,
        prediction_rate: int,
        current_rate: int,
        expected_result: str
) -> None:
    mock_exchange_rate.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
