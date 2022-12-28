import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected_value",
    [
        (95, 95, "Do nothing"),
        (100, 120, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 78, "Sell all your cryptocurrency"),
        (100, 114, "Buy more cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 109, "Buy more cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_cryptocurrency(
        mock_function: mock,
        current_rate: int,
        prediction_rate: int,
        expected_value: str
) -> None:
    mock_function.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_value
