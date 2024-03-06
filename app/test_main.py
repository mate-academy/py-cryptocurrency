import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_value, current_value, expected_result",
    [
        pytest.param(
            105.00,
            100,
            "Do nothing",
        ),
        pytest.param(
            95.00,
            100,
            "Do nothing"
        )
    ]
)
def test_crypto_currency(
        predicted_value: float,
        current_value: float,
        expected_result: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction", MagicMock(return_value=predicted_value)):
        assert cryptocurrency_action(current_value) == expected_result
