import pytest
from typing import Dict, Union
from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action

test_cases = [
    {
        "prediction": 11,
        "expected": "Buy more cryptocurrency",
        "description": "Rate increased > 1.05",
    },
    {
        "prediction": 10,
        "expected": "Do nothing",
        "description": "Stable rate (between 9.5 and 10.5)",
    },
    {
        "prediction": 10.5,
        "expected": "Do nothing",
        "description": "Exactly 5% increase - do nothing",
    },
    {
        "prediction": 9.5,
        "expected": "Do nothing",
        "description": "Exactly 5% drop - do nothing",
    },
    {
        "prediction": 4,
        "expected": "Sell all your cryptocurrency",
        "description": "Rate decreased < 0.95 ",
    }
]


@pytest.mark.parametrize(
    "test_case",
    test_cases,
    ids=[case["description"] for case in test_cases]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: MagicMock,
        test_case: Dict[str, Union[int, float, str]]
) -> None:
    current_rate = 10

    mock_prediction.return_value = test_case["prediction"]

    result = cryptocurrency_action(current_rate)
    assert result == test_case["expected"]

    mock_prediction.assert_called_once_with(current_rate)
