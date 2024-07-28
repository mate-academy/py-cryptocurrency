from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mock_return_value,func_value,expected_result",
    [
        pytest.param(
            220,  # This ensures the ratio > 1.05
            100,
            "Buy more cryptocurrency",
            id="should buy more cryptocurrency"
        ),
        pytest.param(
            50,  # This ensures the ratio < 0.95
            200,
            "Sell all your cryptocurrency",
            id="should sell cryptocurrency"
        ),
        pytest.param(
            105,
            100,
            "Do nothing",
            id="should do nothing when 1.5"
        ),
        pytest.param(
            95,
            100,
            "Do nothing",
            id="should do nothing when 0.95"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency(mock_get_exchange_rate_prediction: mock.Mock,
                        mock_return_value: int,
                        func_value: int,
                        expected_result: str) -> None:
    mock_get_exchange_rate_prediction.return_value = mock_return_value
    assert cryptocurrency_action(func_value) == expected_result
